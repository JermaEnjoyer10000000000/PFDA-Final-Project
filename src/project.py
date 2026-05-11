import pygame
import pyperclip
import yt_dlp

pygame.init()

pygame.key.set_repeat(400, 50)

class InputBox:

    def __init__(self, x, y, w, h):

        self.rect = pygame.Rect(x, y, w, h)

        self.color_inactive = (150, 150, 150)
        self.color_active = (100, 149, 237)

        self.color = self.color_inactive

        self.text = ""

        self.font = pygame.font.SysFont("Arial", 24)

        self.active = False 

    def handle_event(self, event):

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

            self.color = (
                self.color_active
                if self.active
                else self.color_inactive
            )

        # Keyboard input
        if event.type == pygame.KEYDOWN and self.active:

            # CTRL + V Paste
            if (
                event.key == pygame.K_v
                and pygame.key.get_mods() & pygame.KMOD_CTRL
            ):

                self.text += pyperclip.paste()

            # Backspace
            elif event.key == pygame.K_BACKSPACE:

                self.text = self.text[:-1]

            # Enter
            elif event.key == pygame.K_RETURN:

                self.active = False
                self.color = self.color_inactive

            # Normal typing
            else:

                self.text += event.unicode

    def draw(self, screen):

        # Render text
        text_surface = self.font.render(
            self.text,
            True,
            (0, 0, 0)
        )

        # Draw text
        screen.blit(
            text_surface,
            (self.rect.x + 5, self.rect.y + 5)
        )

        # Draw border
        pygame.draw.rect(
            screen,
            self.color,
            self.rect,
            2
        )

class Button:

    def __init__(self, x, y, w, h, text, color):

        self.rect = pygame.Rect(x, y, w, h)

        self.text = text

        self.color = color

        self.font = pygame.font.SysFont("Arial", 24)

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            self.color,
            self.rect
        )

        text_surface = self.font.render(
            self.text,
            True,
            (255, 255, 255)
        )

        text_rect = text_surface.get_rect(
            center=self.rect.center
        )

        screen.blit(text_surface, text_rect)

    def clicked(self, pos):

        return self.rect.collidepoint(pos)

class VideoDownloadTool:

    def __init__(self):

        # Window setup
        self.WIDTH = 900
        self.HEIGHT = 600

        self.screen = pygame.display.set_mode(
            (self.WIDTH, self.HEIGHT)
        )

        pygame.display.set_caption(
            "Video Downloader"
        )

        self.clock = pygame.time.Clock()

        self.running = True

        # Font
        self.font = pygame.font.SysFont(
            "Arial",
            24
        )

        # Input box
        self.input_box = InputBox(
            50,
            60,
            800,
            40
        )

        # Buttons
        self.load_button = Button(
            150,
            140,
            250,
            50,
            "Load Video Info",
            (50, 205, 50)
        )

        self.download_button = Button(
            500,
            140,
            250,
            50,
            "Download Video",
            (100, 149, 237)
        )

        # Status message
        self.message = ""

        # Video info
        self.video_title = ""

        self.video = []


    def draw_text(self, text, x, y, color=(0, 0, 0)):

        rendered_text = self.font.render(
            text,
            True,
            color
        )

        self.screen.blit(
            rendered_text,
            (x, y)
        )

    def get_videos(self):

        try:

            ydl_opts = {
                'quiet': True,
                'skip_download': True
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:

                info = ydl.extract_info(
                    self.input_box.text,
                    download=False
                )

                self.video_title = info.get(
                    "title",
                    "Unknown Title"
                )

                self.videos = info.get(
                    "formats",
                    []
                )

                self.message = "Video Loaded Successfully!"

        except Exception as e:

            self.message = f"Error: {e}"


    def download_video(self):

        try:

            import os

            # Create downloads folder
            download_folder = "downloads"

            if not os.path.exists(download_folder):
                os.makedirs(download_folder)

            self.message = "Downloading..."

            ydl_opts = {

                # Highest quality video + audio
                'format': 'bestvideo+bestaudio/best',

                # Save location
                'outtmpl': os.path.join(
                    download_folder,
                    '%(title)s.%(ext)s'
                ),

                # Merge final output into MP4
                'merge_output_format': 'mp4',

                # Show terminal progress
                'quiet': False,

                # Better YouTube compatibility
                'extractor_args': {
                    'youtube': {
                        'player_client': ['android']
                    }
                }
            }

            # Download video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:

                ydl.download(
                    [self.input_box.text]
                )

            self.message = (
                "Download Complete with Audio!"
            )

        except Exception as e:

            self.message = (
                f"Download Failed: {e}"
            )


    def handle_events(self):

        for event in pygame.event.get():

            # Quit
            if event.type == pygame.QUIT:

                self.running = False

            # Input handling
            self.input_box.handle_event(event)

            # Mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Load video info
                if self.load_button.clicked(event.pos):

                    if self.input_box.text.strip() == "":

                        self.message = "Please enter a YouTube URL!"

                    else:

                        self.get_videos()

                # Download video
                if self.download_button.clicked(event.pos):

                    if self.input_box.text.strip() == "":

                        self.message = "Please enter a YouTube URL!"

                    else:

                        self.download_video()


    def draw(self):

        self.screen.fill((255, 255, 255))

        # Title
        self.draw_text(
            "YouTube Video Downloader",
            50,
            10,
            (100, 149, 237)
        )

        # Input label
        self.draw_text(
            "Enter YouTube URL:",
            50,
            35
        )

        # Input box
        self.input_box.draw(self.screen)

        # Buttons
        self.load_button.draw(self.screen)

        self.download_button.draw(self.screen)

        # Video title
        if self.video_title != "":

            self.draw_text(
                f"Title: {self.video_title}",
                50,
                250,
                (0, 100, 0)
            )

        # Status message
        self.draw_text(
            self.message,
            50,
            320,
            (255, 0, 0)
        )

        # Instructions
        self.draw_text(
            "Tip: Use CTRL + V to paste URLs",
            50,
            500,
            (100, 100, 100)
        )

        pygame.display.flip()
        

    def run(self):

        while self.running:

            self.handle_events()

            self.draw()

            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":

    tool = VideoDownloadTool()

    tool.run()
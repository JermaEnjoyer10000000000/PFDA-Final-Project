import pygame
from pytube import YouTube

pygame.init()

# Set window size and title
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("YouTube Downloader")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 149, 237)
GREEN = (50, 205, 50)
RED = (255, 0, 0)

# Fonts
font = pygame.font.SysFont("Arial", 24)

# UI Elements
input_box = pygame.Rect(50, 50, 700, 40)

# Variables
url_text = ""
active_input = False
message = ""
available_streams = []
buttons = []

def draw_text(surface, text, position, color=BLACK):
    rendered_text = font.render(text, True, color)
    surface.blit(rendered_text, position)

# Function to get available streams
def get_available_streams(url):
    global available_streams, message, buttons

    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True)

        available_streams = list(streams)
        buttons = []

        y_pos = 150

        for i, stream in enumerate(available_streams):
            label = f"{stream.resolution} - {stream.mime_type}"
            button_rect = pygame.Rect(50, y_pos, 500, 40)

            buttons.append({
                "rect": button_rect,
                "stream": stream,
                "label": label
            })

            y_pos += 60

        message = "Streams loaded successfully!"

    except Exception as e:
        message = f"Error fetching streams: {e}"
    
    def download_stream(stream):
        global message

    try:
        stream.download()
        message = "Download Complete!"

    except Exception as e:
        message = f"Download failed: {e}"


    # Main loop
running = True

while running:
    screen.fill(WHITE)

    # Draw title
    draw_text(screen, "YouTube Video Downloader", (50, 10), BLUE)

    # Event handling
    for event in pygame.event.get():

        # Quit event
        if event.type == pygame.QUIT:
            running = False

        # Mouse click event
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Input box click
            if input_box.collidepoint(event.pos):
                active_input = True
            else:
                active_input = False

            # Check button clicks
            for button in buttons:
                if button["rect"].collidepoint(event.pos):

                    if url_text.strip() == "":
                        message = "Please enter URL!"
                    else:
                        download_stream(button["stream"])

            # Load streams button
            load_button = pygame.Rect(600, 100, 150, 40)

            if load_button.collidepoint(event.pos):
                if url_text.strip() == "":
                    message = "Please enter URL!"
                else:
                    get_available_streams(url_text)

                     # Keyboard input
        if event.type == pygame.KEYDOWN and active_input:

            if event.key == pygame.K_BACKSPACE:
                url_text = url_text[:-1]

            elif event.key == pygame.K_RETURN:
                active_input = False

            else:
                url_text += event.unicode


            #If event is MOUSEBUTTONDOWN:
                #If click inside input box:
                    #Set active_input = TRUE
                #Else:
                    #Set active_input = FALSE
                
                #If click inside any download button:
                    #If url_text is empty:
                        #Set message = "Please enter URL!"
                    #Else:
                        #If available_streams is empty:
                            #Call get_available_streams(url_text)
                        #Call download_stream(selected stream)

            #If event is KEYDOWN AND active_input is TRUE:
                #If key is BACKSPACE:
                    #Remove last character from url_text
                #Else If key is RETURN:
                    #Set active_input = FALSE
                #Else:
                    #Append key character to url_text

        #Draw input box and url_text
        #Draw download buttons for available_streams
        #Draw message

        #Update Pygame display

#End Loop

#Quit Pygame
#End
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


# ---------------------------------------------------
# Button Class
# ---------------------------------------------------
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
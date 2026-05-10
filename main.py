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

#Function draw_text(surface, text, position, color):
    #// Render and display text on the screen
    #RENDER text using font
    #Blit text to surface at position

#Function get_available_streams(url):
    #Set Try and except
    #Try
        #yt = YouTube(url)
        #streams = yt.streams
        #Filter streams by type (video/audio) and resolution
        #Store stream objects in available_streams list
    #Catch Exception
        #Set message = "Error fetching streams"

#Function download_stream(stream):
    #Try
        #Call stream.download()
        #Set message = "Download Complete!"
    #Catch Exception
        #Set message = "Download failed"

#MAIN LOOP:
    #While running:
        #Fill screen with background color

        #For each event in Pygame events:
            #If event is quit:
                #Stop loop

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

#Initialize Pygame
#Set window size and title
#Define colors, fonts, and UI elements (input box, buttons, messages)

#CREATE variables:
    #url_text = ""           // stores URL input by user
    #active_input = FALSE    // tracks if input box is active
    #message = ""            // status messages
    #available_streams = []  // list of available formats/qualities

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
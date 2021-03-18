#   --------------
#   Imports
#   --------------
import os
from os import startfile
import random
import glob
import pygame
import pygame_gui

#   --------------
#   WINDOW                              <- Window
#   --------------
#window = Tk()                                                   #   Create blank window
#window.geometry('300x150')                                      #   Set window size
#window.title("ranMediaFind")                                    #   Window Title
#windowTitle = Label(window, text="Open random jonVid")          #   Create Label
#windowTitle.pack()                                              #   Set label location

#   --------------
#   pygame
#   --------------
pygame.init()                                                   #   Start pygame

pygame.display.set_caption('ranMediaFind')                      #   Title window
window_surface = pygame.display.set_mode((300, 150))            #   Set window size

background = pygame.Surface(300, 150)                           #   Window inner size
background.fill(pygame.Color('#000000'))                        #   Set window background to black

manager = pygame_gui.UIManager((300, 150))                      #   Create a UIManger

clock = pygame.time.Clock()                                     #   Create clock
is_running = True                                               #   Set variable, is_running, to true

while is_running:                                               #   Loop while is_running = True

    time_delta = clock.tick(60)/1000.0                                      #   set tick speed

    for event in pygame.event.get():                                        #   Listen for pygame events
        if event.type == pygame.QUIT:                                           #   Check for event: pygame.QUIT
            is_running = False                                                      #   Stop program

        manager.process_events(event)                                           #  Load events through the UIManager

    manager.update(time_delta)                                              #   Connect UIManger with time

    window_surface.blit(background, (0, 0))                     #   Draw image at 0, 0
    manager.draw_ui(window_surface)                             #   Create ui within the UIManager

    pygame.display.update()                                     #   Load pygame update

#   --------------
#   BUTTON                              <- Button
#   --------------
#def genBtn():                                                   #   Define button press command
    #   --------------
    #   Find random .jonVid             <- Find random .jonVid
    #   --------------
 #   vids = []                                                               #   Create list

 #   for jonVid in glob.glob("./media/**/*.jonVid", recursive = True):       #   Grab all files inside ./media with the file extension .jonVid
 #       vids.append(jonVid)                                                    #   Pack every occurance into the list vids

#    rFile = vids[random.randint(0, len(vids))]                              #   Grab random vid from list
#    print(rFile)                                                            #   Print random vid

#    windowTitle.configure(text="Opening: \n" +                              #   Display button press
#     (os.path.splitext(os.path.basename(rFile))[0]))                        #   Shows the name of file opened with out the directory or the file extension

#    startfile(rFile)                                                        #   Open random vid

#gen = Button(window, text="Generate", command=genBtn)           #   Display generate button
#gen.pack()                                                      #   Allign button

#   --------------
#   TEXT BOX                            <- Text box
#   --------------
#findTitle = Label(window, text="\nFind jonVid")                 #   Create new label with the text Find jonVid
#findTitle.pack()                                                #   Allign new label
#find = Entry(window, width=10)                                  #   Create text box
#find.pack()                                                     #   Allign new text box


#   --------------
#   DISPLAY WINDOW                      <- Display window
#   --------------
#window.mainloop()                                               #   Start window
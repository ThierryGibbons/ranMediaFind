#   IMPORTS
#   --------------
import os
from os import startfile
import random
import glob
import pygame
import pygame_gui
#   /IMPORTS
#   --------------

filterSel = []
menuChanged = False

#   PYGAME
#   --------------
pygame.init()                                                   #   Start pygame

pygame.display.set_caption('ranMediaFind')                      #   Title window
window_surface = pygame.display.set_mode((300, 400))            #   Set window size (300, 150) not (800, 600)

background = pygame.Surface((300, 400))                         #   Window inner size
background.fill(pygame.Color('#000000'))                        #   Set window background to black

manager = pygame_gui.UIManager((300, 400))                      #   Create a UIManger

genButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 50), (100, 50)),
                                            text='Generate',
                                            manager=manager)

filterList = ['no filter', 'movies', 'shorts', 'tv shows']

filterMenu = pygame_gui.elements.UIDropDownMenu(options_list=filterList, starting_option='Filter',
                                                relative_rect=pygame.Rect((100,100), (100,50)),
                                                manager=manager)

clock = pygame.time.Clock()                                     #   Create clock
is_running = True                                               #   Set variable, is_running, to true

def noSpace(string):
    return string.replace(" ", "")

while is_running:                                               #   Loop while is_running = True

    time_delta = clock.tick(60)/1000.0                                      #   set tick speed

    for event in pygame.event.get():                                        #   Listen for pygame events
        if event.type == pygame.QUIT:                                           #   Check for event: pygame.QUIT
            is_running = False                                                      #   Stop program


        #   DROPDOWN MENU CHANGE
        #   --------------

        
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if noSpace(event.text)=='movies' or noSpace(event.text)=='shorts' or noSpace(event.text)=='tvshows':
                    print('Selected:  ', event.text)
                    filterSel = event.text
                    menuChanged = True
                if noSpace(event.text)=='nofilter':
                    menuChanged = False
                
        #   BUTTON PUSH
        #   --------------
        if event.type == pygame.USEREVENT:                                      #   Listen for pygame user event
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:                    #   Check if any button was pressed
                if event.ui_element == genButton:                                      #   Check if button was genButton
                    vids = []

                    if menuChanged == True:
                        print('Finding ', filterSel)
                        if filterSel=='movies' or filterSel=='shorts' or filterSel=='tv shows':
                            for jonVid in glob.glob('media/' + noSpace(filterSel) + '/**/*.jonVid', recursive = True):
                                vids.append(jonVid)
                            
                            rFile = vids[random.randint(0, len(vids))]
                            print(rFile)

                            print("Opening: " +
                             os.path.splitext(os.path.basename(rFile))[0])
                        
                            startfile(rFile)

                    else:
                        for jonVid in glob.glob('media/**/*.jonVid', recursive = True):
                            vids.append(jonVid)

                        rFile = vids[random.randint(0, len(vids))]
                        print(rFile)

                        print("Opening: " +                                                     #   Display button press
                         (os.path.splitext(os.path.basename(rFile))[0]))                        #   Shows the name of file opened with out the directory or the file extension

                        startfile(rFile)

        #   /BUTTON PUSH
        #   --------------

        manager.process_events(event)                                           #  Load events through the UIManager

    manager.update(time_delta)                                              #   Connect UIManger with time

    window_surface.blit(background, (0, 0))                     #   Draw image at 0, 0
    manager.draw_ui(window_surface)                             #   Create ui within the UIManager

    pygame.display.update()                                     #   Load pygame update
    #   /PYGAME
    #   --------------
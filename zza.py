#   --------------
#   Imports
#   --------------
import os
from os import startfile
import random
import glob
from tkinter import *

#   --------------
#   WINDOW                              <- Window
#   --------------
window = Tk()                                                   #   Create blank window
window.geometry('300x150')                                      #   Set window size
window.title("ranMediaFind")                                    #   Window Title
windowTitle = Label(window, text="Open random jonVid")          #   Create Label
windowTitle.pack()                                              #   Set label location

#   --------------
#   BUTTON                              <- Button
#   --------------
def genBtn():                                                   #   Define button press command
    #   --------------
    #   Find random .jonVid             <- Find random .jonVid
    #   --------------
    vids = []                                                               #   Create list

    for jonVid in glob.glob("./media/**/*.jonVid", recursive = True):       #   Grab all files inside ./media with the file extension .jonVid
        vids.append(jonVid)                                                 #   Pack every occurance into the list vids

    rFile = vids[random.randint(0, len(vids))]                              #   Grab random vid from list
    print(rFile)                                                            #   Print random vid

    windowTitle.configure(text="Opening: \n" +                              #   Display button press
     (os.path.splitext(os.path.basename(rFile))[0]))                        #   Shows the name of file opened with out the directory or the file extension

    startfile(rFile)                                                        #   Open random vid

gen = Button(window, text="Generate", command=genBtn)           #   Display generate button
gen.pack()                                                      #   Allign button

#   --------------
#   TEXT BOX                            <- Text box
#   --------------
findTitle = Label(window, text="\nFind jonVid")                 #   Create new label with the text Find jonVid
findTitle.pack()                                                #   Allign new label
find = Entry(window, width=10)                                  #   Create text box
find.pack()                                                     #   Allign new text box


#   --------------
#   DISPLAY WINDOW                      <- Display window
#   --------------
window.mainloop()                                               #   Start window
#   TODO: Create GUI

import random
import glob

#   create vids list
vids = []


#   grab all files inside ./media with the file extension .jonVid
for jonVid in glob.glob("./media/**/*.jonVid", recursive = True): 
    #   pack every occurance into the list vids
    vids.append(jonVid)

#   print random item from list
print(vids[random.randint(0, len(vids))])
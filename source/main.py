# ebay scrapper - C.R.G. 2018
# main file
# uses sav.py, ui.py and scrape.py

import sav
import ui
import scrape

# set name for save file
cfile = 'sav.csv'
# read the data from save file
aUrl = sav.fread(cfile)
#print aUrl

# main loop
# prompt user to select the program's new action
opt = ui.mainScr(aUrl, cfile)

# user exited program
if opt == 0:
    # save data
    sav.fwrite(cfile, aUrl)
    print 'Program closed by user ( EXIT )'

# user input - gets input from user and shows data on screen

import scrape

delim = '#'
null = 'null'
selected = 'xxx'

# main options screen
def mainScr(arr, cfile):
    print '\n>> Please select an option:'
    print '1=Search on ebay / 2=Add new / 3=Delete data / 4=Backup / 0=Quit'
    op = input('Option: ')
    while op != 0:
        if op == 1:
            print 'searching...'
            scrape.LoopTroughItems(arr)
        elif op == 2:
            if addScr():
                item = getItem()
                scrape.ArrAdd(item, arr)
                print '1 item added'
        elif op == 3:
            if delScr():
                item = getItem()
                scrape.ArrRem(item, arr)
                print '1 item deleted'
        else:
            if bakScr():
                scrape.BakFile(cfile, arr)
        # check for given value again
        op = mainScr(arr, cfile)
    return op

# get value of item
def getItem(): return selected

# add new item value
def setItem(new):
    global selected
    selected = new

# select item
def selScr():
    item = input("Enter the item's code: ")
    print 'You have selected item:', item
    return str(item)

# add an element
def addScr():
    print '>> Add a new search element:'
    sel = selScr()
    op = input('Save item? 1=yes / 0=no ')
    if op == 1:
        setItem(sel)
        return True
    else:
        return False

# delete an element
def delScr():
    print '>> !!! Delete unneeded searches !!!'
    sel = selScr()
    op = input('Are you sure you want to delete this item? 2=yes / 0=no ')
    if op == 2:
        setItem(sel)
        return True
    else:
        return False

# make a backup to the save file ( returns true/false )
def bakScr():
    print '>> You will create a backup to the data file.'
    op = input('Proceed? 1=yes / 0=no ')
    if op == 1:
        return True
    else:
        return False

######## CRG ebay scrapper v.1.2.4 ########
Done using python 2.7.14

## Table of contents:
1. Info

2. License

3. Contact

###########################################

## 1. Info
First of all, I'd like to thank to Kenneth Reitz on https://docs.python-guide.org/scenarios/scrape/

This program was created and tested under Windows XP and 7 using Python 2.7.14 so, if any 
conflicts may appear under a different version of Windows or Python please contact the 
maker. Contact details are given under section 3.

All data is scraped from Ebay and saved in the 'sav.csv' file located in the root folder 
of this application.

The data is saved and loaded in this form:
	Item_code_1\n
	Item_code_2\n
	...
Where \n is the newline escape sequence ( enter if you modify the file manually ).

The 'backup.csv' file holds the same data and, as its name implies, it is the backup file 
of 'sav.csv'

The app's files ( source folder ):
	main.py		// main file - this is where you run the app
	sav.py		// handles saving and retrieving data from the '.xml' file
	scrape.py	// handles the proceess of scraping data from ebay
	ui.py		// handles user input and output to screen
	readme.md	// reamde/info file ( yeah..this one )
	license.md	// contains the license of this app and source code

## 2. License
The license of this software and its source-code is based on the zlib/libpng license. 

See file 'license.md' for more info.

## 3. Contact
2011 - 2018 Radu Claudiu a.k.a. CRG.

http://crgames.elementfx.com/

cla.radu@crgames.elementfx.com

###########################################

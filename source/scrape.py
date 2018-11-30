# scrapping html files for specific data
# thanks to Kenneth Reitz on https://docs.python-guide.org/scenarios/scrape/

from lxml import html
import requests

delim = '#'
clink = 'https://www.ebay.com/itm/'

# get the filename
def getFile(): return cfile

# search ebay for stuff
def SrcBay():
    print 'Searching...'

# add data to the global array
def ArrAdd(new, aUrl):
    if new != '':
        aUrl.append(new)

# remove data from the global array
def ArrRem(elem, aUrl):
    aUrl.remove(elem)

# make a backup to the data file
def BakFile(fname, aUrl):
    # open file for writing and create if it doesn't exist
    f = open('backup.csv', 'w+')
    # append data
    for a in aUrl:
        f.write(a + '\n')
    print 'Backup created for file [', fname, '].'

# scrape ebay page for data
def Scrape(item, size):
    cpage = clink+item
    # get data from page
    page = requests.get(cpage)
    tree = html.fromstring(page.content)
    # create lists from the info table on ebay
    itemt = tree.xpath('//h1[@id="itemTitle"]/text()')
#    itemt = tree.xpath('//h1[@class="it-ttl"]/text()')
    cond = tree.xpath('//div[@id="vi-itm-cond"]/text()')
#    cond = tree.xpath('//div[@class="u-flL lable"]/text()')
    avail = tree.xpath('//span[@id="qtySubTxt"]/span/text()')
#    avail = tree.xpath('//div[@class="qtyTxt vi-bboxrev-dsplblk  vi-qty-fixAlignment feedbackON"]/text()')
    sold11 = tree.xpath('//span[@class="vi-qtyS  vi-qty-vert-algn vi-qty-pur-lnk"]/a/text()')
    sold12 = tree.xpath('//span[@class="vi-qtyS-hot  vi-qty-vert-algn vi-qty-pur-lnk"]/a/text()')
    sold13 = tree.xpath('//span[@class="vi-qtyS-hot-red  vi-qty-vert-algn vi-qty-pur-lnk"]/a/text()')
    sold21 = tree.xpath('//span[@class="vi-qtyS  vi-bboxrev-dsplblk vi-qty-vert-algn vi-qty-pur-lnk"]/a/text()')
    sold22 = tree.xpath('//span[@class="vi-qtyS-hot  vi-bboxrev-dsplblk vi-qty-vert-algn vi-qty-pur-lnk"]/a/text()')
    sold23 = tree.xpath('//span[@class="vi-qtyS-hot-red  vi-bboxrev-dsplblk vi-qty-vert-algn vi-qty-pur-lnk"]/a/text()')
    if len(sold11) > 0:
        sold = sold11[0]
    elif len(sold12) > 0:
        sold = sold12[0]
    elif len(sold13) > 0:
        sold = sold13[0]
    elif len(sold21) > 0:
        sold = sold21[0]
    elif len(sold22) > 0:
        sold = sold22[0]
    elif len(sold23) > 0:
        sold = sold23[0]
    else:
        sold = '0 sold'
    price = tree.xpath('//span[@id="prcIsum"]/text()')
    # check if array contains any data
    alen = len(itemt)
    # show results
    if alen > 0:
        availt = avail[0].strip('\t\n')
        print '> Item (', item, '):\n', itemt[0]
        print '[ condition:', cond[0], '| price:', price[0], '|', availt, '|', sold, ']\n'
    else:
        print '0 item(s) found:', item, '\n'

# looping trough the array of items
def LoopTroughItems(arr):
    for item in arr:
        Scrape(item, 0)
        # deprecated
#        fin = item.split(delim)
#        Scrape(fin[0], fin[1])

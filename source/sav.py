# saving and retrieving data to and from a '.csv' file

import os.path

br = '\n'

# read data from file
def fread(fname):
	# create an empty array
	a = []
	# first, check if file exists
	if os.path.exists(fname):
		# file found so open it for reading
		f = open(fname, 'r')
		# now, loop trough the file line by line
		for n in f:
			# save data to array
			a.append(n.replace(br,''))
	else:
		# file not found so create it
		f = open(fname, 'w+')
		print "File ", fname, " was created successfully!"
	return a

# save data to a file
def fwrite(fname, data):
        f = open(fname, 'w')
        for n in data:
                f.write(n + br)
        print("Data saved!")

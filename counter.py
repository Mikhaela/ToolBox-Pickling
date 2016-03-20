""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists 
#Return True if path refers to an existing path. 
#Returns False for broken symbolic links. 
import sys
import pickle
from pickle import dump, load

def update_counter(file_name, reset=False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be rest.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
	"""

	counter = 0 

	# If file dne or reset = True we will create counter starting at 1 
	if exists(file_name) == False or reset == True: 
		f  = open(file_name,'w') # f is now a file object ready to be written
		counter = 1 # set counter ready to write to file 
		pickle.dump(counter,f)
		return counter
		f.close()

	# If file exist and reset = False we will add one to counter
	elif exists(file_name) and reset == False: 
		f = open(file_name,'r+') # f is now a file object ready to be read and then written 
		counter = pickle.load(f) # load f as file already exists
		f.seek(0,0) # moves pointer to start of file to write over previous content
		counter += 1 # adds 1 to pre-existing counter
		pickle.dump(counter,f) # update counter in f 
		return counter 
		f.close() 
		
if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1])) # catches name variable 


	# I had a hard time with this, my main difficulty was in sorting out the order of operations to call 
	# 1) open/create file
	# 2) if file contains content: load content with pickle
	# 3) dump new content into file
	# 4) return content & close file 



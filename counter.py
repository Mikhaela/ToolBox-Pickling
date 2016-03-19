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


	if exists(file_name) == False or reset == True: # if file dne or reset = True
		f = open(file_name,'w') # f is now a file object ready to be written
		counter = 1
		pickle.load(f)
		f.write(str(counter)) # writes counter to file
		f.close()
		pickle.dump()
		print 

	elif exists(file_name) and reset == False: # if file exist and reset = False add one to counter
		counter += 1 # adds 1 to pre-existing counter
		f = open(file_name,'r+') # f is now a file object ready to be read
		content = pickle.load(f) # load instead of dump as f already exists
		f.seek(0,0) # moves pointer to start of file to write over previous content
		f.write(str(counter)) # writes counter to file
		f.close()

		
	

update_counter("blah.txt")
		
# if __name__ == '__main__':
# 	if len(sys.argv) < 2:
# 		import doctest
# 		doctest.testmod()
# 	else:
# 		print "new value is " + str(update_counter(sys.argv[1])) # catches name variable 



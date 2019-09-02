# Aaron Himan
# CS 4375 Theory of Operating Systems
# Intro to Python Lab
# Based strongly off of the given code for the python-intro lab by Dr. Fruedenthaul, specifically
# in the wordCountTest.py program. I also referenced python3 docs, mainly the re documentation
# found at https://docs.python.org/3/library/re.html.

# To run the program, run the command: python3 wordCount.py <input text file> <output text file>

#! usr/env/ python3

import sys   # command line arguments
import re    # regular expression tools
import os    # checking if files exist

# set input and output files
if len(sys.argv) is not 3:
	print("Correct usage: wordCount.py <input text file> <output text file>")
	exit()

inputFileName= sys.argv[1]
outputFileName= sys.argv[2]

# make sure text files exist
if not os.path.exists(inputFileName):
	print ("text file input %s doesn't exist! Exiting" % inputFileName)
	exit()

# make a master dictionary like countTest example. words will be key, # of times will be val
master = {}

# read the text file to count
with open(inputFileName, 'r') as inputFile:  # r is read only mode
	for line in inputFile:
		# remove newline characters
		line = line.strip() # removes leading and ending characters of arg

		# make all lowercase since case insensitive
		line = line.lower()

		# replace hypenated words to two words seperated **fixed hyphenated word errors
		line = re.sub(r'-', ' ',line)

		# replace apostraphe with two seperate words **fixed apostrophe errors
		line = re.sub(r'\'', ' ', line)

		# remove punctuation using re
		line = re.sub(r'[^\w\s]','',line) # sub all not words or spaces

		# split line by white space or punctuation
		words = re.split('[ \t]', line)

		# put words into dictionary. the word is the key, the # of times the word is val
		for word in words:
				if word in master:
					master[word] = master[word] + 1 # increment counter/val for the word
				else:
					master[word] = 1 # first use of word

# space is being counted, need to remove
master.pop('', None)   # removes space from the dictionary

# write master dictionary into file
with open(outputFileName, "w") as outputFile:

	# sort dictionary and write into file
	for key, val in sorted(master.items()):
		outputFile.write("%s %s\n" % (key, val))
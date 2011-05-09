#!/usr/bin/python

### bsn-gen.py
### 
### A small program to generate a number of valid BSNs.
###
### This program was written by mrngm

import sys

def print_readme():
	print """bsn-gen.py [number] [from] [distance]

Generates [number] of valid BSNs
[number]	Number of BSNs to generate
[from]		8 or 9 digit BSN to start from
[distance]	add <distance> to the next BSN to be generated

When no number is given, this help message is displayed.
This script was made by mrngm, source at https://github.com/mrngm/python-misc/
"""

# Generates the checkdigit for a 7 or 8 digit BSN
# and prepends a 0 if necessary
def generate_checkdigit(bsn):
	if len(bsn) > 8:
		sys.exit("Number is too long, exiting");
	elif len(bsn) == 7 and bsn.isdigit():
		fullbsn = "0" + bsn[0:len(bsn)]
	elif len(bsn) == 8 and bsn.isdigit():
		fullbsn = bsn
	else:
		sys.exit("Generate_checkdigit: Number too short or not a number, exiting")

	total = 0
	for i in range(8):
		total += int(bsn[i])*(9-i)
	checkdigit = total % 11
	if checkdigit is 10:
		checkdigit = 0
	return checkdigit

def generate_next(prev, distance):
	if len(prev) > 9:
		sys.exit("Number is too long, exiting");
	elif len(prev) == 8 and prev.isdigit():
		fullprev = "0" + prev[0:len(prev)]
	elif len(prev) == 9 and prev.isdigit():
		fullprev = prev
	else:
		sys.exit("Generate_next: Number too short or not a prev, exiting");

	# strip the last digit, this is the check digit
	strnumber = increase_bsn(prev, distance)
	checkdigit = generate_checkdigit(strnumber)
	strnumber = strnumber + str(checkdigit)
	return strnumber

def increase_bsn(bsn, number):
	fullnumber = int(bsn[0:len(bsn)-1])
	fullnumber += number
	strnumber = str(fullnumber)
	for i in range(8-len(strnumber)):
		strnumber = "0" + strnumber
	return strnumber

def generate(bsn, distance, number):
	bsn = generate_next(bsn, distance)
	print bsn
	for i in range(number):
		bsn = generate_next(bsn, distance)
		print bsn



if len(sys.argv) < 2:
	# print README
	print_readme()
elif len(sys.argv) == 2:
	# generate sys.argv[1] number of BSNs
	generate("123456789", 1, int(sys.argv[1]))
elif len(sys.argv) == 3:
	# generate sys.argv[1] number of BSNs starting from sys.argv[2]
	generate(sys.argv[2], 1, int(sys.argv[1]))
elif len(sys.argv) == 4:
	# Same as above, but skip sys.argv[3] BSNs, creating gaps
	generate(sys.argv[2], int(sys.argv[3]), int(sys.argv[1]))
else:
	# catchall, print README
	print_readme()

#!/usr/bin/python

### bsn-gen.py
### 
### A small program to generate a number of valid BSNs.
###
### This program was written by mrngm

import sys

def print_readme():
	print """bsn-gen.py [number] [from]

Generates [number] of valid BSNs
[number]	Number of BSNs to generate
[from]		8 or 9 digit BSN to start from

When no number is given, this help message is displayed.
This script was made by mrngm, source at https://github.com/mrngm/python-misc/
"""

# Generates the checkdigit for a 7 or 8 digit BSN
# and prepends a 0 if necessary
def generate_checkdigit(bsn):
	if len(prev) > 8:
		sys.exit("Number is too long, exiting");
	elif len(number) == 7 and number.isdigit():
		fullnumber = "0" + number[0:len(number)]
	elif len(number) == 8 and number.isdigit():
		fullnumber = number
	else:
		sys.exit("Number too short or not a number, exiting")

	total = 0
	for i in range(8):
		total += int(bsn[i])*(9-i)
	checkdigit = total % 11
	return checkdigit

def generate_next(prev):
	if len(prev) > 9:
		sys.exit("Number is too long, exiting");
	elif len(number) == 8 and number.isdigit():
		fullnumber = "0" + number[0:len(number)]
	elif len(number) == 9 and number.isdigit():
		fullnumber = number
	else:
		sys.exit("Number too short or not a number, exiting");

	# strip the last digit, this is the check digit
	fullnumber = int(fullnumber[0:len(number)-1])
	fullnumber++
	checkdigit = generate_checkdigit(str(fullnumber))
	fullnumber = str(fullnumber) + str(checkdigit)
	return fullnumber



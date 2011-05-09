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
	return checkdigit

def generate_next(prev):
	if len(prev) > 9:
		sys.exit("Number is too long, exiting");
	elif len(prev) == 8 and prev.isdigit():
		fullprev = "0" + prev[0:len(prev)]
	elif len(prev) == 9 and prev.isdigit():
		fullprev = prev
	else:
		sys.exit("Generate_next: Number too short or not a prev, exiting");

	# strip the last digit, this is the check digit
	fullnumber = int(prev[0:len(prev)-1])
	fullnumber += 1
	strnumber = str(fullnumber)
	for i in range(8-len(strnumber)):
		strnumber = "0" + strnumber
	checkdigit = generate_checkdigit(strnumber))
	strnumber = strnumber + str(checkdigit)
	return strnumber


if len(sys.argv) < 2:
	# print README
	print_readme()
elif len(sys.argv) == 2:
	# generate sys.argv[1] number of BSNs
	for i in range(int(sys.argv[1])):
		print generate_next("123456789")
elif len(sys.argv) == 3:
	# generate sys.argv[1] number of BSNs starting from sys.argv[2]
	for i in range(int(sys.argv[1])):
		print generate_next(sys.argv[2])
else:
	# catchall, print README
	print_readme()

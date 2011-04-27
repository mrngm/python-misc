#!/usr/bin/python

### bsn-check.py
### 
### A small program to check whether a BSN is a valid one, by evaluating
### the eleven test.
###
### This program was written by mrngm

import sys

def print_readme():
	print """bsn-check.py [number]

Checks whether number is a valid BSN.
[number]	BSN to check

When no number is given, this help message is displayed.
This script was made by mrngm, source at https://github.com/mrngm/python-misc/
"""

def eleven_test(number):
	if len(number) > 9:
		sys.exit("Number is too long, exiting");
	elif len(number) == 8 and number.isdigit():
		fullnumber = "0" + number[0:len(number)]
	elif len(number) == 9 and number.isdigit():
		fullnumber = number
	else:
		sys.exit("Number too short or not a number, exiting");
	
	total = 0
	for i in range(8):
		total += int(fullnumber[i])*(9-i)
		print "Fullnumber["+str(i)+"]="+fullnumber[i]+", multiplier: " + str(9-i) + " Total: " + str(total)
	checkdigit = total / 11
	print "Check digit raw: "+str(checkdigit)
	if checkdigit == 10:
		checkdigit = 0
	print "BSN: " + fullnumber + ", check digit: " + str(checkdigit)
	if checkdigit == int(fullnumber[8]):
		print "BSN is valid!"
	else:
		print "BSN is NOT valid."


if len(sys.argv) < 2:
	# print README
	print_readme()
elif len(sys.argv) == 2:
	# do the eleven check
	eleven_test(sys.argv[1])

#!/usr/bin/python

import sys

def print_readme():
	print """bsn-check.py [number]

Checks whether number is a valid BSN.
[number]	BSN to check

When no number is given, this help message is displayed.
This script was made by mrngm, source at https://github.com/mrngm/python-misc/
"""

if len(sys.argv) < 2:
	# print README
	print_readme()
elif len(sys.argv) == 2:
	# do the eleven check
	print "Eleven check here"

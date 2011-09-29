#!/usr/bin/env python2

import sys
import os
import commands
import re
import datetime

def print_readme():
	print """etherlocator.py <mac-addr> [location_file]

<mac-addr>       The MAC address of the station you want to locate
[location-file]  (optional) File containing all the locations
"""

def request_info(macaddr):
	today = datetime.date.today()
	dag = today.strftime('%d/%m')
	info = { "macaddr": macaddr }
	etheroutput = commands.getoutput("ethergids " + info['macaddr'])
	info['ether'] = etheroutput.splitlines()
	info['ether'] = info['ether'][1:]
	src = re.compile(dag)
	info['result'] = list()
	for item in info['ether']:
		match = src.search(item)
		if match != None:
			info['result'].append(ethergids_to_dict(match.string))
	return info

def ethergids_to_dict(str):
	splitted = re.split('\s+', str)
	info = dict()
	info['macaddr'] = splitted[0]
	info['date']    = splitted[1]
	info['ipaddr']  = splitted[2]
	info['swport']  = splitted[3]
	if 'ap-huyg' in splitted[3]:
		info['loc'] = location_from_ap(splitted[3])
	info['name']    = splitted[5]
	return info

def location_from_ap(ap):
	# standard: read file 'ap_locations.txt'
	global ap_file
	txt = open(ap_file, 'r')
	splitted = txt.readlines()
	ap = re.split('/', ap)
	zoek = re.compile(ap[0])
	for item in splitted:
		match = zoek.search(item)
		if match != None:
			apmatch = match.string
			apmatch = re.split('\s+', apmatch)
			aploc = apmatch[4]
	return aploc

def print_info(information):
	print "Requested information for MAC address " + information['macaddr'] + ":"
	for i in information['result']:
		print """[""" + i['macaddr'] + """]:
	Date:        """ + i['date'] + """
	IP address:  """ + i['ipaddr'] + """
	Switchport:  """ + i['swport'] + """
	Location:    """ + i['loc'] + """
	Name:        """ + i['name'] + """
"""

ap_file = 'ap_locations.txt'

if len(sys.argv) < 2:
	print_readme()
elif len(sys.argv) >= 2:
	if len(sys.argv) == 3:
		ap_file = sys.argv[2]
	information = request_info(sys.argv[1])
	print_info(information)
	


# vim: set background=dark:

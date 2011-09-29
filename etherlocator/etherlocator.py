#!/usr/bin/env python2

import sys
import os
import commands
import re
import datetime

def print_readme():
	print """etherlocator.py <mac-addr> [dd/mm] [location_file]

<mac-addr>       The MAC address of the station you want to locate
[dd/mm]          (optional) The date for lookup
[location-file]  (optional) File containing all the locations
"""

def request_info(macaddr, dag):
	today = datetime.date.today()
	if dag == None:
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
		print "Die is der"
		info['loc'] = location_from_ap(splitted[3])
	else:
		print "Nee hoor"
		info['loc'] = splitted[4]
	info['name']    = splitted[5]
	return info

def location_from_ap(ap):
	# standard: read file 'ap_locations.txt'
	global ap_file
	aploc = '???'
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
elif len(sys.argv) == 2:
	information = request_info(sys.argv[1])
	print_info(information)
elif len(sys.argv) == 3:
	if len(sys.argv[2]) == 5 and '/' in sys.argv[2]:
		dag = sys.argv[2] # assuming ap_file != 'ap/bl'
		information = request_info(sys.argv[1], dag)
	else:
		ap_file = sys.argv[2]
		information = request_info(sys.argv[1], '')
	print_info(information)
elif len(sys.argv) == 4:
	dag = sys.argv[2]
	ap_file = sys.argv[3]
	information = request_info(sys.argv[1], dag)
	print_info(information)


# vim: set background=dark:

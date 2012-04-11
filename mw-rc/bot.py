import sys
import socket
import string
import thread
import subprocess

HOST="irc.server.org"
PORT=6667
NICK="WikiRC"
IDENT="wikirc"
CHANNEL="#recent-changes"
REALNAME="Wiki RecentChanges"
readbuffer=""

s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))

UDP_IP="127.0.0.1"
UDP_PORT=65423

sock = socket.socket( socket.AF_INET, # Internet
                      socket.SOCK_DGRAM ) # UDP
sock.bind( (UDP_IP,UDP_PORT) )
joined=0
auth=0
threaded=0

#s.setblocking(0)
#sock.setblocking(0)

def udpblup(s,*arg):
	while 1:
		data, addr = sock.recvfrom(1024)
		print "UDP::Message: ", data
		s.send("PRIVMSG " + CHANNEL + " :" + data)

while 1:
	try:
		readbuffer=readbuffer+s.recv(1024)
		temp=string.split(readbuffer, "\n")
		readbuffer=temp.pop( )

		for line in temp:
			line=string.rstrip(line)
			line=string.split(line)

			if(line[0]=="PING"):
				s.send("PONG %s\r\n" % line[1])
			if (len(line) > 2):
				if(line[1]=="NOTICE" and line[2] == "Auth" and line[3] == ":Welcome"):
					auth=1
			if (len(line) >= 5):
				if(line[3]==":" + NICK + ":" and line[4] == "src"):
					s.send("PRIVMSG " + CHANNEL + " :src at https://github.com/mrngm/python-misc/tree/master/mw-rc/\r\n")
			print line

		if (joined == 0 and auth == 1):
			s.send("JOIN " + CHANNEL + "\r\n")
			joined = 1
		if (joined == 1 and auth == 1 and threaded == 0):
			thread.start_new_thread(udpblup, (s,1))
			threaded = 1
	except socket.error:
		continue

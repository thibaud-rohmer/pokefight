import asyncore
import collections
import logging
import socket
import time
import sys
import getopt
import random
import asyncore
sys.path.append('./Classes');

### My Classes ###
from Pokemon import *
from Types import *
from Pokedex import *
from PokeFight import *
from Server import *


class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg

def main(argv=None):
	server = "localhost"
	port = 0
	
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "s:p:c:d",[])
		except getopt.error, msg:
			raise Usage(msg)
			
		# option processing
		for option, value in opts:
			if option == "-s":
				server = value
			if option == "-p":
				port = int(value)
			if option == "-c":
				Fight.choices = int(value)
			if option == "-d":
				logging.basicConfig(level=logging.INFO)
	except Usage, err:
		print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
		print >> sys.stderr, "\t for help use --help"
		exit(0)
		
	logging.info('Creating host')
	host = Host((server,port))
	(h,p) = host.getsockname()
	print "Host : ",h," Port : ",p
	print "To connect, type : "
	print "python client.py -s ",h," -p ",p," -n NICK"
	asyncore.loop()
	
	
	
if __name__ == '__main__':
	sys.exit(main())
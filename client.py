import asyncore
import collections
import logging
import socket
import sys
import getopt
import time
sys.path.append('./Classes');

### My Classes ###
from Pokemon import *
from Client import *

class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg


def main(argv=None):

	s = socket.socket()         # Create a socket object
	host = socket.gethostname() # Get local machine name
	port = 54171
	name = "Alice"
	
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "s:p:n:bdc",[])
		except getopt.error, msg:
			raise Usage(msg)
			
		# option processing
		for option, value in opts:
			if option == "-s":
				host = value
			if option == "-p":
				port = int(value)
			if option == "-n":
				name = value
			if option == "-b":
				Pokemon.boobs = True
			if option == "-d":
				logging.basicConfig(level=logging.INFO)
			if option == "-c":
				TypeColor.color_print = True
	except Usage, err:
		print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
		print >> sys.stderr, "\t for help use --help"
		exit(0)

	logging.info('Creating client')
	print "Waiting for another player to join."
	alice = Client((host,port), name)
	asyncore.loop()
	
if __name__ == '__main__':
	sys.exit(main())

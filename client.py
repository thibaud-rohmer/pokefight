import asyncore
import collections
import logging
import socket
import sys
import getopt
sys.path.append('./Classes');

### My Classes ###
from Pokemon import *

MAX_MESSAGE_LENGTH = 1024

def clear():
	a="\n"
	for i in range(0,200):
		a = a + "\n"
	print a


class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg

class Client(asyncore.dispatcher):

	def __init__(self, host_address, name):
		asyncore.dispatcher.__init__(self)
		self.log = logging.getLogger('Client (%7s)' % name)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.name = name
		self.log.info('Connecting to host at %s', host_address)
		self.connect(host_address)
		self.outbox = collections.deque()
		self.pokemons = [0]*2

	def say(self, message):
		self.outbox.append(message)
		self.log.info('Enqueued message: %s', message)

	def handle_write(self):
		if not self.outbox:
			return
		message = self.outbox.popleft()
		if len(message) > MAX_MESSAGE_LENGTH:
			raise ValueError('Message too long')
		self.send(message)

	def handle_read(self):
		messages = self.recv(MAX_MESSAGE_LENGTH)
		self.log.info("Message Received : %s",messages)

		messages_array = messages.split("\n")
		for message in messages_array:
			self.log.info("Treating message : %s",message)
			
			parsed = message.split("\t")
			code = parsed[0]
	
			if(code == "GO"):
				msg = raw_input("Select Attack [1-4] : ")
				self.send("ATT\t" + str(msg))
				print "Waiting for ",self.pokemons[1].name," to select his attack..."
				
			if(code == 'UPD'):
				# Update lives
				self.pokemons[0].life = int(parsed[1])
				self.pokemons[1].life = int(parsed[2])
				clear()
				self.pokemons[1].disp_front()
				self.pokemons[0].disp_back()
				self.pokemons[0].disp_attak()

			if(code == 'ATT'):
				# Other pokemon attacked
				att_name = parsed[1]
				succ = int(parsed[2])
				crit = int(parsed[3])
				eff  = float(parsed[4])

				msg = self.pokemons[1].name + " used : " + att_name + ". "
			
				if(succ == 0):
					msg = msg + "But it failed ! "
				else:
					if(crit == 1):
						msg = msg + "Critical hit ! "
					if(eff > 1):
						msg = msg + "It's super effective ! "
					if(eff < 1):
						msg = msg + "It's not very effective ... "
				print msg


			if(code == 'HIT'):
				# You got attacked
				att_name = parsed[1]
				succ = int(parsed[2])
				crit = int(parsed[3])
				eff  = float(parsed[4])

				msg = self.pokemons[0].name + " used : " + att_name + ". "
			
				if(succ == 0):
					msg = msg + "But it failed ! "
				else:
					if(crit == 1):
						msg = msg + "Critical hit ! "
					if(eff > 1):
						msg = msg + "It's super effective ! "
					if(eff < 1):
						msg = msg + "It's not very effective ... "
				print msg

			
			if(code == 'LOSE'):
				# End, you lose
				print "You lose."
				exit(0)
			
			if(code == 'WIN'):
				# End, you win
				print "You win."
				exit(0)
			
			if(code == 'POKE'):
				# Infos on a pokemon
				attacks = []
				for i in range(4):
					attacks.append( 
									Attack(
										parsed[(4*i)+5],
										parsed[(4*i)+6],
										int(parsed[(4*i)+7]),
										float(parsed[(4*i)+8])
										)
									)
				self.pokemons[int(parsed[1])] = Pokemon(parsed[2],"",int(parsed[3]),42,42,42,int(parsed[4]),attacks)


def main(argv=None):

	s = socket.socket()         # Create a socket object
	host = socket.gethostname() # Get local machine name
	port = 54171
	name = "Alice"
	
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "s:p:n:",[])
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
	except Usage, err:
		print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
		print >> sys.stderr, "\t for help use --help"
		exit(0)

#	logging.basicConfig(level=logging.INFO)
	logging.info('Creating client')
	alice = Client((host,port), name)
	asyncore.loop()
	
if __name__ == '__main__':
	sys.exit(main())

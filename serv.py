import asyncore
import collections
import logging
import socket
import time
import sys
import getopt
import random
sys.path.append('./Classes');

### My Classes ###
from Pokemon import *
from Types import *
from Pokedex import *

MAX_MESSAGE_LENGTH = 1024


class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg

class Fight():
	
	pokedex = -1
	
	def __init__(self,p1,p2,c1,c2):
		self.p1 = p1
		self.p2 = p2
		self.c1 = c1
		self.c2 = c2
		self.a1 = -1
		self.a2 = -1

class Fights():
	fights = []
	
	@classmethod
	def get_fight(self,s):
		for f in self.fights:
			if(f.c1.socket == s or f.c2.socket == s):
				return f
		return -1

class RemoteClient(asyncore.dispatcher):

	"""Wraps a remote client socket."""

	def __init__(self, host, socket, address):
		asyncore.dispatcher.__init__(self, socket)
		self.host = host
		self.outbox = collections.deque()
		self.socket = socket
		self.av_pok = []
		self.informed = False

	def say(self, message):
		self.outbox.append(message)
		
	def handle_read(self):
		client_message = self.recv(MAX_MESSAGE_LENGTH)
		print "message received : ",client_message
		messages = client_message.split("\n")
		for message in messages:
			parsed = message.split("\t")
			code = parsed[0]
			
			f = Fights.get_fight(self.socket)
			if(f.c1.socket == self.socket):
				pos = 1
			else:
				pos = 2
				
			if(code=="CHOSEN"):
				if(pos==1):
					if(f.a1 == -1):
						try:
							if(int(parsed[1]) > len(self.av_pok) or int(parsed[1]) < 1):
								raise Exception
							f.p1 = self.av_pok[int(parsed[1]) - 1]
							print "Number 1 selected ", f.p1.name
						except:
							f.c1.say("CHOOSE\t")
				else:
					try:
						if(int(parsed[1]) > len(self.av_pok) or int(parsed[1]) < 1):
							raise Exception
						f.p2 = self.av_pok[int(parsed[1]) - 1]
						print "Number 2 selected ", f.p2.name
					except:
						f.c2.say("CHOOSE\t")
				if(f.p1 != -1 and f.p2 != -1):
					self.informfight(f)

			if(code=="ATT"):
				if(pos==1):
					if(f.a1 == -1):
						try:
							if(int(parsed[1]) > 4 or int(parsed[1]) < 1):
								raise Exception
							f.a1 = int(parsed[1]) 
							print "Attacking using ", f.a1
						except:
							f.c1.say("GO\t")
				else:
					try:
						if(int(parsed[1]) > 4 or int(parsed[1]) < 1):
							raise Exception
						f.a2 = int(parsed[1])
						print "Attacking using ", f.a2
					except:
						f.c2.say("GO\t")
				
				print f.a1,f.a2
				if(f.a1 != -1 and f.a2 != -1):
					# Attacks

					
					att 		= 	f.p1.attacks[int(f.a1) - 1]
					success 	= 	Pokemon.success(f.p1,f.p2,att)
					critical 	= 	Pokemon.critical(f.p1)
					eff 		=	Types.get_eff(f.p2.type,att.type)
					f.p2.hit(f.p1,f.p2,att,success,critical,eff)
					f.c2.send("ATT\t" + att.name + "\t" + str(success) + "\t" + str(critical) + "\t" + str(eff))
					f.c1.send("HIT\t" + att.name + "\t" + str(success) + "\t" + str(critical) + "\t" + str(eff))

					time.sleep(2)
										
					if(f.p2.life <= 0):
						f.c1.send("WIN\t\n")
						f.c2.send("LOSE\t\n")

					att 		= 	f.p2.attacks[int(f.a2) - 1]
					success 	= 	Pokemon.success(f.p2,f.p1,att)
					critical 	= 	Pokemon.critical(f.p2)
					eff 		=	Types.get_eff(f.p1.type,att.type)
					f.p1.hit(f.p2,f.p1,att,success,critical,eff)
					f.c1.send("ATT\t" + att.name + "\t" + str(success) + "\t" + str(critical) + "\t" + str(eff))
					f.c2.send("HIT\t" + att.name + "\t" + str(success) + "\t" + str(critical) + "\t" + str(eff))
					time.sleep(2)

					if(f.p1.life <= 0):
						f.c2.send("WIN\t\n")
						f.c1.send("LOSE\t\n")
					
					f.a1 = -1
					f.a2 = -1
					print f.p1
					print f.p2
					
					message = "UPD\t"+ str(f.p1.life) + "\t" + str(f.p2.life) + "\t\n"
					f.c1.say(message)
					message = "UPD\t"+ str(f.p2.life) + "\t" + str(f.p1.life) + "\t\n"
					f.c2.say(message)
					
					f.c1.say("GO\t\n")
					f.c2.say("GO\t\n")
			
			if(code == "WHO"):
				f = Fights.get_fight(self.socket)
				if(f.c1.socket == self.socket):
					f.n1 = parsed[1]
					f.c2.say("ADV\t"+parsed[1]+"\t\n")
					# message = "UPD\t"+ str(f.p2.life) + "\t" + str(f.p1.life) + "\t\n"
					# f.c2.say(message)
					# f.c2.say("GO\t\n")
				else:
					f.n2 = parsed[1]
					f.c1.say("ADV\t"+parsed[1]+"\t\n")
					# message = "UPD\t"+ str(f.p1.life) + "\t" + str(f.p2.life) + "\t\n"
					# f.c1.say(message)
					# f.c1.say("GO\t\n")
				self.informed = True
				print "informed"
				if(f.c1.informed and f.c2.informed):
					self.informchoices(f,3)	
			
	def informfight(self,f):
		message = f.p1.to_socket()
		f.c1.say("POKE\t0\t" + message)
		f.c2.say("POKE\t1\t" + message)
	
		message = f.p2.to_socket()
		f.c1.say("POKE\t1\t"+message)
		f.c2.say("POKE\t0\t"+message)

		message = "UPD\t"+ str(f.p1.life) + "\t" + str(f.p2.life) + "\t\n"
		f.c1.say(message)
		message = "UPD\t"+ str(f.p2.life) + "\t" + str(f.p1.life) + "\t\n"
		f.c2.say(message)
			
		f.c1.say("GO\t\n")
		f.c2.say("GO\t\n")
	

	def informchoices(self,f,number):
		for p in [f.c1,f.c2]:
			for i in range(number):
				fail = 1
				while(fail==1):
					try:
						P1 = Fight.pokedex.get_pok(random.randint(0,151),5)
						fail = 0
					except:
						fail = 1
				p.av_pok.append(P1)
				
		for p in f.c1.av_pok:
			f.c1.say("AV\t" + p.to_socket() + "\t\n")
			f.c2.say("ADVAV\t" + p.to_socket() + "\t\n")
		
		for p in f.c2.av_pok:
			f.c2.say("AV\t" + p.to_socket() + "\t\n")
			f.c1.say("ADVAV\t" + p.to_socket() + "\t\n")
			
		f.c1.say("CHOOSE\t\n")
		f.c2.say("CHOOSE\t\n")
				
	def handle_write(self):
		if not self.outbox:
			return
		message = self.outbox.popleft()
		if len(message) > MAX_MESSAGE_LENGTH:
			raise ValueError('Message too long')
		self.send(message)


class Host(asyncore.dispatcher):

	log = logging.getLogger('Host')
	
	def __init__(self, address=('localhost', 0)):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.bind(address)
		self.listen(1)
		self.remote_clients = []
		self.fighters = []
		self.fights = []
		Fight.pokedex = Pokedex()
		Types.main()

	def handle_accept(self):
		socket, addr = self.accept() # For the remote client.
		self.log.info('Accepted client at %s', addr)
		self.remote_clients.append(RemoteClient(self, socket, addr))
		self.fighters.append(self.remote_clients[-1])
		if(len(self.fighters) == 2):
			f=Fight(-1,-1,self.fighters[0],self.fighters[1])
			Fights.fights.append(f)
			self.fighters = []
			f=Fights.get_fight(socket)
			f.c1.say("WHO\t\n")
			f.c2.say("WHO\t\n")
		
	def handle_read(self):
		print self.socket
		self.log.info('Received message: %s', self.read())

	def broadcast(self, message):
		self.log.info('Broadcasting message: %s', message)
		for remote_client in self.remote_clients:
			remote_client.say(message)


def main(argv=None):
	
	server = "localhost"
	port = 0
	
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "s:p:d",[])
		except getopt.error, msg:
			raise Usage(msg)
			
		# option processing
		for option, value in opts:
			if option == "-s":
				server = value
			if option == "-p":
				port = int(value)
			if option == "-d":
				logging.basicConfig(level=logging.INFO)
	except Usage, err:
		print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
		print >> sys.stderr, "\t for help use --help"
		exit(0)
		
	
#	logging.basicConfig(level=logging.INFO)
	logging.info('Creating host')
	host = Host((server,port))
	(h,p) = host.getsockname()
	print "Host : ",h," Port : ",p
	print "To connect, type : "
	print "python client.py -s ",h," -p ",p," -n NICK"
	asyncore.loop()
	
	
	
if __name__ == '__main__':
	sys.exit(main())
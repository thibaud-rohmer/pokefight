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

MAX_MESSAGE_LENGTH = 1024

class RemoteClient(asyncore.dispatcher):

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
			if(f.client[0].socket == self.socket):
				pos = 0
			else:
				pos = 1

			if(code=="CHOSEN"):
				if(f.attack[pos] == -1):
					try:
						if(int(parsed[1]) > len(self.av_pok) or int(parsed[1]) < 1):
							raise Exception
						f.pokemon[pos] = self.av_pok[int(parsed[1]) - 1]
						print "Number ",pos," selected ",f.pokemon[pos].name
					except:
						f.client[pos].say("CHOOSE\t")
				if(f.pokemon[0] != -1 and f.pokemon[1] != -1):
					self.informfight(f)

			if(code=="ATT"):
				if(f.attack[pos] == -1):
					try:
						if(int(parsed[1]) > 4 or int(parsed[1]) < 1):
							raise Exception
						f.attack[pos] = int(parsed[1]) 
						print "Attacking using ", f.attack[pos]
					except:
						f.client[pos].say("GO\t")

				if(f.attack[0] != -1 and f.attack[1] != -1):
					f.handle_attacks()

			if(code == "WHO"):
				f = Fights.get_fight(self.socket)
				if(f.client[0].socket == self.socket):
					f.n1 = parsed[1]
					f.client[1].say("ADV\t"+parsed[1]+"\t\n")
				else:
					f.n2 = parsed[1]
					f.client[0].say("ADV\t"+parsed[1]+"\t\n")

				self.informed = True
				if(f.client[0].informed and f.client[1].informed):
					self.informchoices(f,Fight.choices)	

	def informfight(self,f):
		message = f.pokemon[0].to_socket()
		f.client[0].say("POKE\t0\t" + message)
		f.client[1].say("POKE\t1\t" + message)

		message = f.pokemon[1].to_socket()
		f.client[0].say("POKE\t1\t"+message)
		f.client[1].say("POKE\t0\t"+message)

		f.client[0].say("GO\t\n")
		f.client[1].say("GO\t\n")


	def informchoices(self,f,number):
		for p in [f.client[0],f.client[1]]:
			for i in range(number):
				fail = 1
				while(fail==1):
					try:
						P1 = Fight.pokedex.get_pok(random.randint(0,151),5)
						for k in p.av_pok:
							if(P1.name == k.name):
								raise Exception
						fail = 0
					except:
						fail = 1
				p.av_pok.append(P1)

		for p in f.client[0].av_pok:
			f.client[0].say("AV\t" + p.to_socket() + "\t\n")
			f.client[1].say("ADVAV\t" + p.to_socket() + "\t\n")

		for p in f.client[1].av_pok:
			f.client[1].say("AV\t" + p.to_socket() + "\t\n")
			f.client[0].say("ADVAV\t" + p.to_socket() + "\t\n")

		f.client[0].say("CHOOSE\t\n")
		f.client[1].say("CHOOSE\t\n")

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
			f.client[0].say("WHO\t\n")
			f.client[1].say("WHO\t\n")
		
	def handle_read(self):
		print self.socket
		self.log.info('Received message: %s', self.read())

	def broadcast(self, message):
		self.log.info('Broadcasting message: %s', message)
		for remote_client in self.remote_clients:
			remote_client.say(message)

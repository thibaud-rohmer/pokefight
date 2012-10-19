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

MAX_MESSAGE_LENGTH = 1024




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
		self.adv = ""
		self.AV = []
		self.ADVAV = []

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

	def handle_connect(self):
		pass
		
	def printscreen(self):
		print ""
		print "================================================================================"		
		print "Playing against : \t", self.adv
		print "================================================================================"		
		self.pokemons[1].disp_front()
		self.pokemons[0].disp_back()
		print "================================================================================"
		
	def handle_read(self):
		messages = self.recv(MAX_MESSAGE_LENGTH)
		self.log.info("Message Received : %s",messages)

		messages_array = messages.split("\n")
		for message in messages_array:
			self.log.info("Treating message : %s",message)
			
			parsed = message.split("\t")
			code = parsed[0]
			if(code == "ADV"):
				self.adv = parsed[1]

			if(code == "WHO"):
				msg = "WHO\t"+str(self.name)+"\t\n"
				self.send(msg)
				
			if(code == "GO"):
				self.printscreen()
				self.pokemons[0].disp_attak()
				print ""
				msg = raw_input("Select Attack [1-4] : ")
				self.send("ATT\t" + str(msg))
				self.clear()
				print ""
				print "Waiting for ",self.pokemons[1].name," to select his attack..."
				print ""
				
			if(code == 'UPD'):
				self.pokemons[0].life = int(parsed[1])

			if(code == 'EUPD'):
				self.pokemons[1].life = int(parsed[1])

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
						
				# self.printscreen()
				print msg
				
			if(code == 'HIE'):
				if(parsed[1]=="STOP"):
					self.pokemons[0].affected = ""
				else:
					self.pokemons[0].affected = parsed[1]
					print self.pokemons[0].name, " is ", self.pokemons[0].affected, " !"

			if(code == 'ATE'):
				if(parsed[1]=="STOP"):
					self.pokemons[0].affected = ""
				else:
					self.pokemons[1].affected = parsed[1]
					print self.pokemons[1].name, " is ", self.pokemons[1].affected, " !"
					
			if(code == 'AFF'):
				print self.pokemons[0].name, parsed[1]
				
			if(code == 'EAFF'):
				print self.pokemons[1].name, parsed[1]
				
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
					if(eff < 1 and eff > 0):
						msg = msg + "It's not very effective ... "
					if(eff == 0):
						msg = msg + "It doesn't do anything ! "
				# self.printscreen()
				print msg
				
			if(code == 'END'):
				if(parsed[1]=='0'):
					print "You lose."
				if(parsed[1]=='1'):
					print "You win."
				if(parsed[1]=='2'):
					print "Nobody wins !"
				exit(0)
			
			if(code == 'AV'):
				self.AV.append([parsed[1],parsed[2]])
			
			if(code == 'ADVAV'):
				self.ADVAV.append([parsed[1],parsed[2]])
				
			if(code == 'CHOOSE'):
				self.clear()
				print "Playing against : \t", self.adv
				print "================================================================================"		
				print self.adv," can choose among :"
				for i in range(len(self.ADVAV)):
					pika = self.ADVAV[i]
					print "\t",str(i+1),". ",TypeColor.getcol(pika[1]),pika[0]," - ",pika[1],TypeColor.clear()
				print "You may choose among :"
				for i in range(len(self.AV)):
					pika = self.AV[i]
					print "\t",str(i+1),". ",TypeColor.getcol(pika[1]),pika[0]," - ",pika[1],TypeColor.clear()
				msg = raw_input("Select Pokemon [1-"+str(len(self.AV))+"] : ")
				self.send("CHOSEN\t" + str(msg))
				print "Waiting for ", self.adv, " to select his pokemon..."
				
			if(code == 'POKE'):
				# Infos on a pokemon
				attacks = []
				for i in range(4):
					attacks.append( 
									Attack(
										parsed[(4*i)+6],
										parsed[(4*i)+7],
										int(parsed[(4*i)+8]),
										float(parsed[(4*i)+9])
										)
									)
				self.pokemons[int(parsed[1])] = Pokemon(parsed[2],parsed[3],int(parsed[4]),42,42,42,int(parsed[5]),attacks)
				self.clear()
				
	def clear(self):
		a="\n"
		for i in range(0,200):
			a = a + "\n"
		print a

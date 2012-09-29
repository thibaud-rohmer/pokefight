#!/usr/bin/python           # This is server.py file
import sys
import time
sys.path.append('./Classes');

### My Classes ###
from Pokemon import *


import socket               # Import socket module
s1 = socket.socket()         # Create a socket object

host = socket.gethostname() # Get local machine name
s1.bind((host, 0))        # Bind to the port


print 'Server started!'
print 'Waiting for players...'

(h,p) = s1.getsockname()
print 'Port :', p
s1.listen(5)                 # Now wait for client connection.


while True:
	client_1, addr1 = s1.accept()
	print 'First player  : \t', addr1

	client_2, addr2 = s1.accept()
	print 'Second player : \t', addr2

	# Initialize pokemons
	P1a1 = Attack("Morsure",20)
	P1a2 = Attack("Griffe",10)
	P1a3 = Attack("Eclair",25)
	P1a4 = Attack("Foudre",30)

	P2a1 = Attack("Flash",10)
	P2a2 = Attack("Flamme",15)
	P2a3 = Attack("Griffe",10)
	P2a4 = Attack("Morsure",20)

	P1 = Pokemon("Pikachu",100,10,[P1a1,P1a2,P1a3,P1a4],"^_^"," o/")
	P2 = Pokemon("Salameche",100,30,[P2a1,P2a2,P2a3,P2a4],"*_*"," p/")


	turn = 0

	# Send pokemons to players
	message = P1.to_socket()
	client_1.send("POKE\t0\t" + message)
	client_2.send("POKE\t1\t" + message)
	time.sleep(.1)

	message = P2.to_socket()
	client_1.send("POKE\t1\t"+message)
	client_2.send("POKE\t0\t"+message)
	time.sleep(.1)

	# Start Fight
	end_fight = False;
	while not end_fight:
		turn = 1-turn
		if(turn==1):
			c1 	= 	client_1
			c2 	=	client_2
			p1	=	P1
			p2	=	P2
		else:
			c1	=	client_2
			c2	=	client_1
			p1	=	P2
			p2	=	P1
		
		message = "LIVES\t"+ str(p1.life) + "\t" + str(p2.life) + "\t"
		c1.send(message)
		message = "LIVES\t"+ str(p2.life) + "\t" + str(p1.life) + "\t"
		c2.send(message)
		time.sleep(.1)
		
		att_number = "hello"
		while(not(isinstance(att_number,int))):
			c1.send("GO\t")
			try:
				att_number = int(c1.recv(1024))
				if(att_number < 1 or att_number > 4):
					att_number = "hello"
			except:
				pass	
		att = p1.attacks[int(att_number) - 1]
	
		c2.send("ATT\t"+ att.name +"\t")
		print 'Pokemon utilise : ', att.name
		p2.hit(att.strength)

		time.sleep(2)
		if(p2.life <= 0):
			c1.send("WIN\t")
			c2.send("LOSE\t")
			time.sleep(1)
			end_fight = True

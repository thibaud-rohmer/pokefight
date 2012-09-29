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
c1, addr1 = s1.accept()     # Establish connection with client.
print 'Got connection from', addr1

c2, addr2 = s1.accept()     # Establish connection with client.
print 'Got connection from', addr2



# Start code
P1a1 = Attack("Morsure",20)
P1a2 = Attack("Griffe",10)
P1a3 = Attack("Eclair",25)
P1a4 = Attack("Fourde",30)

P2a1 = Attack("Flash",10)
P2a2 = Attack("Flamme",15)
P2a3 = Attack("Griffe",10)
P2a4 = Attack("Morsure",20)

P1 = Pokemon("Pikachu",100,10,[P1a1,P1a2,P1a3,P1a4],"^_^"," o/")
P2 = Pokemon("Salameche",100,30,[P2a1,P2a2,P2a3,P2a4],"*_*"," p/")





# Sending pokemons
c1.send(P1.to_socket());
time.sleep(.1)
c1.send(P2.to_socket());

c2.send(P2.to_socket());
time.sleep(.1)
c2.send(P1.to_socket());

time.sleep(.1)

turn = 0

message = "GO\t"+ str(P1.life) + "\t" + str(P2.life) + "\t\n"
c1.send(message)
message = "GO\t"+ str(P1.life) + "\t" + str(P2.life) + "\t\n"
c2.send(message)

while True:
	turn = 1-turn
	if(turn==1):
		c 	= 	c1
		p1	=	P1
		p2	=	P2
	else:
		c	=	c2
		p1	=	P2
		p2	=	P1
		
	message = "GO\t"+ str(p1.life) + "\t" + str(p2.life) + "\t\n"
	c.send(message)
	att = c.recv(1024)
	print 'Pokemon utilise : ', att
	p2.hit(P1.attacks[int(att) -1].strength)
	message = "DONE\t"+ str(p1.life) + "\t" + str(p2.life) + "\t\n"
	c.send(message)

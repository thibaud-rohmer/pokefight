import socket               # Import socket module
import sys
sys.path.append('./Classes');

### My Classes ###
from Pokemon import *


def clear():
	a="\n"
	for i in range(0,200):
		a = a + "\n"
	print a




s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
host = "threesim.ucd.ie"
port = 4241              # Reserve a port for your service.
port = 17502
 
print 'Connecting to ', host, port
s.connect((host, port))


pokemons = []
for i in range(2):
	msg = s.recv(1024)
	pokemons_sock = msg.split('\n')


	for i in range(len(pokemons_sock)-1) :
		pika = pokemons_sock[i].split('\t')
		attacks = []
		attacks.append(Attack(pika[3],int(pika[4])))
		attacks.append(Attack(pika[5],int(pika[6])))
		attacks.append(Attack(pika[7],int(pika[8])))
		attacks.append(Attack(pika[9],int(pika[10])))
		pokemons.append(Pokemon(pika[0],int(pika[1]),int(pika[2]),attacks,pika[11],pika[12]))


print pokemons

while (pokemons[0].life > 0 and pokemons[1].life > 0):
	for i in range(2):
		msg = s.recv(1024) # Attend l'ordre...
		lives = msg.split('\t')
		pokemons[0].life = int(lives[1])
		pokemons[1].life = int(lives[2])
	
		clear()
		pokemons[1].disp_front()
		pokemons[0].disp_back()
		pokemons[0].disp_attak()
	
	if(pokemons[0].life <= 0 or pokemons[1].life <= 0):
		break
	msg = raw_input("Attaque [1-4] : ")
	s.send(msg)

clear();
if(pokemons[0].life <= 0):
	print "You lose."
	for i in range(4):
		print ""
else:
	print "You win."
	for i in range(4):
		print ""

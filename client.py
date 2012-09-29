import socket               # Import socket module
import sys
import getopt
sys.path.append('./Classes');

### My Classes ###
from Pokemon import *


class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg

def clear():
	a="\n"
	for i in range(0,200):
		a = a + "\n"
	print a


def main(argv=None):

	s = socket.socket()         # Create a socket object
	host = socket.gethostname() # Get local machine name
	port = 54171

	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "s:p:",[])
		except getopt.error, msg:
			raise Usage(msg)
	
		trace = False
		# option processing
		for option, value in opts:
			if option == "-s":
				host = value
			if option == "-p":
				port = int(value)
	except Usage, err:
		print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
		print >> sys.stderr, "\t for help use --help"
		exit(0)

	print 'Connecting to ', host, port
	s.connect((host, port))


	pokemons = [0]*2



	while True:
		msg = s.recv(1024)
		parsed = msg.split('\t')
		code = parsed[0]
		
		if(code == 'LIVES'):
			# Update lives
			pokemons[0].life = int(parsed[1])
			pokemons[1].life = int(parsed[2])
			
			clear()
			pokemons[1].disp_front()
			pokemons[0].disp_back()
			pokemons[0].disp_attak()

		if(code == 'GO'):
			# Select attack	
			msg = raw_input("Select Attack [1-4] : ")
			s.send(msg)

		if(code == 'ATT'):
			# Other pokemon attacked
			print pokemons[1].name + " used : ",parsed[1]

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
			attacks.append(Attack(parsed[5],int(parsed[6])))
			attacks.append(Attack(parsed[7],int(parsed[8])))
			attacks.append(Attack(parsed[9],int(parsed[10])))
			attacks.append(Attack(parsed[11],int(parsed[12])))
			pokemons[int(parsed[1])] = Pokemon(parsed[2],int(parsed[3]),int(parsed[4]),attacks,parsed[13],parsed[14])

if __name__ == "__main__":
	sys.exit(main())
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
			att_name = parsed[1]
			succ = int(parsed[2])
			crit = int(parsed[3])
			eff  = float(parsed[4])

			msg = pokemons[1].name + " used : " + att_name + ". "
			
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

			msg = pokemons[0].name + " used : " + att_name + ". "
			
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
			
			
			pokemons[int(parsed[1])] = Pokemon(parsed[2],"",int(parsed[3]),42,42,42,int(parsed[4]),attacks)

if __name__ == "__main__":
	sys.exit(main())
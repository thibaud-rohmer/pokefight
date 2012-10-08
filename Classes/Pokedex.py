from xml.dom.minidom import parseString
import sys
import time
sys.path.append('./Classes');

### My Classes ###
from Pokemon import *


class Pokedex:
	pokedex = 0
	attdex = 0
	poke_fr = 0
	
	def __init__(self):
		file = open('stuff/pokedata.xml',"r")
		data = file.read()
		file.close()

		#parse the xml
		self.pokedex = parseString(data).getElementsByTagName('pokemon')
		
		file = open('stuff/attdata.xml',"r")
		data = file.read()
		file.close()
		
		self.attdex = parseString(data).getElementsByTagName('move')
		
		file = open('stuff/pok_fr.txt',"r")
		data = file.readlines()
		file.close()
		self.poke_fr = data
	
	def clear_get(self,pokXML,val):
		return pokXML.getElementsByTagName(val)[0].toxml().replace('<'+val+'>','').replace('</'+val+'>','')
		
	def get_att(self, name):
		attXML = -1
		for att in self.attdex:
			if(att.getAttribute("name") == name):
				attXML = att
				break

		if(attXML == -1):
			print "Couldn't find attack ",name,", using random."
			attXML = self.attdex[random.randint(0,len(self.attdex))]
			name = self.clear_get(attXML,'name')


		type 		= 	self.clear_get(attXML,'type')
		strength	=	self.clear_get(attXML,'power')
		accuracy	=	self.clear_get(attXML,'accuracy')

		try:
			t = Types.t[type]
			if(int(strength) < 5):
				raise Exception
			return Attack(name,type,int(strength),float(accuracy))

		except:
			print "Type unknown : ", type
			print "or strength too weak : ", strength
			raise Exception
		
	def get_pok(self, id, level):
		pokXML = self.pokedex[id]
		
		
		name = self.clear_get(pokXML,'name')
		name = self.poke_fr[id][:-1]
		type = self.clear_get(pokXML,'type')
		life = self.clear_get(pokXML,'HP')
		defense = self.clear_get(pokXML,'DEF')
		attack = self.clear_get(pokXML,'ATK')
		speed = self.clear_get(pokXML,'SPD')
		
		print "Looking for attacks for ",name
		attacks = []
		potential_attacks = []
		print "Found ", len(pokXML.getElementsByTagName('move')), " attacks"
		for i in range(len(pokXML.getElementsByTagName('move'))):
			potential_attacks.append(self.clear_get(pokXML.getElementsByTagName('move')[i],'name'))


		while(len(attacks) < 4 and len(potential_attacks) > 0 ):
			try:
				att = self.get_att(potential_attacks.pop(random.randint(0,len(potential_attacks))))
				attacks.append(att)
				i=i+1
			except:
				print "fail"
		while(len(attacks) < 4):
			attacks.append(self.get_att("void"))
		return Pokemon(name,type,int(life),int(attack),int(defense),int(speed),int(level),attacks)
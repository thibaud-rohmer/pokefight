import time
import random

import sys
import time
sys.path.append('./Classes');

### My Classes ###
from Types import *	

class TypeColor():
	color_print = False
	color = { 
			"Normal": 	'\033[1m' ,
			"Grass":  	'\033[42m' ,
			"Electr": 	'\033[93m' ,
			"Water": 	'\033[94m' ,
			"Psychic": 	'\033[95m' ,
			"Ice":   	'\033[96m' ,
			"Bug":    	'\033[97m' ,
			"Ghost":  	'\033[47m\033[30m\033[3m' ,
			"Fire":   	'\033[31m' ,
			"Rock":  	'\033[43m\033[1m\033[34m' ,
			"Fight":  	'\033[1m\033[4m' ,
			"Flying": 	'' ,
			"Ground":	'\033[43m\033[1m' ,
			"Poison":   '\033[45m\033[36m\033[1m' ,
			"Dragon": 	'\033[41m\033[1m' ,
		}
		
	@classmethod
	def getcol(cls,t):
		try:
			if(TypeColor.color_print):
				return TypeColor.color[t]
		except:
			pass
		return ''
	
	@classmethod
	def clear(cls):
		return '\033[0m'


class Effects:
	effects = {
		"ParalysisEffect"	:	"Paralysed",
		"SleepEffect"		:	"Sleeping",
		"PoisonEffect"		:	"Poisoned",
		"BurnEffect"		:	"Burning",
		"FreezeEffect"		:	"Frozen",
		"ConfusionEffect"	:	"Confused"
	}
	
class Attack:
	
	def __init__(self,name,type,strength,accuracy,target="Ennemies",use="",init=""):
		self.name 		= name
		self.strength 	= strength
		self.accuracy 	= accuracy
		self.type 		= type
		self.target		= target
		self.use		= use
		self.init		= init
		self.effect		= -1
		self.effect_proba = 1
		try:
			todo = self.init.split("\n")[2].split("[")[2].split("]")[0].split(",")
			self.effect = Effects.effects[todo[0]]
			self.effect_proba = todo[1]
		except:
			pass
			
	def aff(self):
		print self.get()

	def get(self):
		return TypeColor.getcol(self.type) + self.name + " - " + str(self.type) + TypeColor.clear()
		
	def __repr__(self):
		attrs = vars(self)
		return '\n '.join("%s: %s" % item for item in attrs.items())
		
class Pokemon:
	boobs = False
	
	def __init__(self):
		self.name 		= 	""
		self.life 		= 	10
		self.maxlife 	=	10
		self.level 		= 	1
		self.attacks 	= 	[]
		self.affected 	= 	""

	def __init__(self,name,type,life,attack,defense,speed,level,attacks):
		self.name 		= 	name
		self.type		=	type
		self.life		=	life
		self.maxlife	=	life
		self.attack		=	attack
		self.defense	=	defense
		self.speed		=	speed
		self.level		=	level
		self.attacks	=	attacks
		self.affected 	= 	""		

	def __repr__(self):
		attrs = vars(self)
		return ', '.join("%s: %s" % item for item in attrs.items())

	def ask_attak(self):
		a = "="
		for i in range(65):
			a = a + "="
		print a
		print ""
		self.disp_attak()
		at = self.attacks[input("Attaque : ") - 1]
		return at;

	def disp_attak(self):
		print "1.",self.attacks[0].get(),"\t\t\t\t","2.",self.attacks[1].get()
		print "3.",self.attacks[2].get(),"\t\t\t\t","4.",self.attacks[3].get()
	
	@classmethod
	def success(cls,p1,p2,att):
		proba = att.accuracy
		if(proba == 0):
			proba = 0.80
		print "Success proba : ", proba
		if(random.random() < proba):
			return 1
		else:
			return 0
		
	@classmethod
	def critical(cls,p1):
		proba = float(p1.speed) / 512.0
		print "Critical proba : ", proba
		if(random.random() < proba):
			return 1
		else:
			return 0

	def hit(self,p1,p2,att,success,critical,eff):
		# Yup. This is the true formula, motherfucker.
		if(p1.type == att.type):
			STAB = 1.5
		else:
			STAB = 1.0
		
		modifier = STAB * eff * success * (1+critical) * (1 - random.random()*0.15)
		
		h = ((float(2*p1.level + 10)/250.0) * (float(p1.attack)/float(p2.defense)) * att.strength + 2) * modifier
		self.life = self.life - int(h)
		print int(h)

	def apply_effect(self,at):
		if(random.random() < at.effect_proba):
			if(at.effect != -1):
				self.affected = at.effect
				return True
		return False
	
	def disp_front(self):
		print  TypeColor.getcol(self.type) + self.name + " lvl." + str(self.level) + " - " + self.type + TypeColor.clear() + " " + self.affected
		if(Pokemon.boobs):
			print self.get_life() + "\t\t\t\t\t" + "(o Y o)"
		else:
			print self.get_life() + "\t\t\t\t\t" + "*_*"
		print ""
		print ""
		print ""

	def disp_back(self):
		a = "\t"
		for i in range(5):
			a = a + "\t"
		print a + TypeColor.getcol(self.type) + self.name + " lvl." + str(self.level) + " - " + self.type + TypeColor.clear() + " " + self.affected
		if(Pokemon.boobs):
			print "(_,_) " + a + self.get_life()
		else:
			print "\o/ " + a + self.get_life()
		print ""
	
	def get_life(self):
		a = "["
		for i in range(0, (10 * self.life) / self.maxlife):
			a = a + "="
		for i in range( (10 * self.life) / self.maxlife, 10):
			a = a + " "
		a = a + "]"
		return a


	def disp_attacking(self,at):
		clear()
		print "\t\t\t" + self.name + " used " + at.name
		if(random.randint(0,at.strength) < self.level):
			for i in range(5):
				print ""
			try:
				input()
			except:
				pass
			return True
		else:
			print "\t\t\t But it failed !"
			for i in range(5):
				print ""
			try:
				input()
			except:
				pass
			return False

	def to_socket(self):
		s = self.name + "\t"  + self.type + "\t" + str(self.maxlife) + "\t" +str(self.level) + "\t"
		for i in range(4):
			s = s + self.attacks[i].name + "\t" + self.attacks[i].type + "\t" + str(self.attacks[i].strength) + "\t" + str(self.attacks[i].accuracy) + "\t"
		s = s + "\n"
		return s


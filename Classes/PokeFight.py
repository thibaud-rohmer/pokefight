import time
import random

import sys
import time
import asyncore
sys.path.append('./Classes');

from Pokemon import *
from Pokedex import *

class Fight():
	
	pokedex = -1
	choices = 3
	
	def __init__(self,p1,p2,c1,c2):
		self.pokemon = [p1,p2]
		self.client = [c1,c2]
		self.attack = [-1,-1]
		
		
	def check_life(self,i):
		if(self.pokemon[1-i].life <= 0):
			if(self.pokemon[i].life <= 0):
				self.client[i].send("END\t2\t\n")
				self.client[1-i].send("END\t2\t\n")
			else:	
				self.client[i].send("END\t1\t\n")
				self.client[1-i].send("END\t0\t\n")		
		elif(self.pokemon[i].life <= 0):
				self.client[i].send("END\t0\t\n")
				self.client[1-i].send("END\t1\t\n")
		
		
	def handle_attacks(self):
		
		order_table = self.get_order()
		effect_order_table = []
		for i in order_table:
			att		= 	self.pokemon[i].attacks[int(self.attack[i]) - 1]
			
			self.handle_pre_effects(i)
			self.check_life(i)
			
			if(self.handle_attack_effects(i)):
				effect_order_table.append(i)

			self.check_life(i)
					
			self.client[1-i].say("UPD\t"+ str(self.pokemon[1-i].life)+"\t\n")
			self.client[i].say("EUPD\t"+ str(self.pokemon[1-i].life)+"\t\n")

		for i in effect_order_table:
			self.handle_post_effects(i)
			
			self.client[1-i].say("UPD\t"+ str(self.pokemon[1-i].life)+"\t\n")
			self.client[i].say("EUPD\t"+ str(self.pokemon[1-i].life)+"\t\n")
			self.check_life(i)
			
		
		self.attack[0] = -1
		self.attack[1] = -1

		self.client[0].say("GO\t\n")
		self.client[1].say("GO\t\n")
		
	def handle_pre_effects(self,i):
		pass	
		
	def handle_attack_effects(self,i):
		
		# Take care of effects
		if(self.pokemon[i].affected == "Paralysed"):
			if(random.random() < 0.25):
				self.client[i].send("AFF\tis paralysed, it can't attack.\t\n")
				self.client[1-i].send("EAFF\tis paralysed, it can't attack.\t\n")
				return False

		if(self.pokemon[i].affected == "Sleeping"):
			# Wear off proba
			if(random.random() < 0.5):
				self.client[i].send("AFF\tis sleeping, it can't attack.\t\n")
				self.client[1-i].send("EAFF\tis sleeping, it can't attack.\t\n")
				return False
			else:
				self.client[i].affected = ""
				self.client[1-i].send("HIE\tSTOP\t\n")
				self.client[i].send("ATE\tSTOP\t\n")				
				self.client[i].send("AFF\twoke up !\t\n")
				self.client[1-i].send("EAFF\twoke up !\t\n")
	
		if(self.pokemon[i].affected == "Frozen"):
			# Wear off proba
			if(random.random() < 0.5):
				self.client[i].send("AFF\tis frozen, it can't attack.\t\n")
				self.client[1-i].send("EAFF\tis frozen, it can't attack.\t\n")
				return False
			else:
				self.client[i].affected = ""
				self.client[1-i].send("HIE\tSTOP\t\n")
				self.client[i].send("ATE\tSTOP\t\n")				
				self.client[i].send("AFF\tis unfrozen !\t\n")
				self.client[1-i].send("EAFF\tis unfrozen !\t\n")
		
		if(self.pokemon[i].affected == "Confused"):
			self.client[i].send("AFF\tis confused...\t\n")
			self.client[1-i].send("EAFF\tis confused...\t\n")
			
			# Wear off proba
			if(random.random() < 0.5):
				# Hit yourself proba
				if(random.random() < 0.5):
					conf = Attack("confusion","none",40,100)
					self.pokemon[i].hit(self.pokemon[i],self.pokemon[i],conf,1,0,1)				
				
					# Update lives
					self.client[i].say("UPD\t"+ str(self.pokemon[i].life)+"\t\n")
					self.client[1-i].say("EUPD\t"+ str(self.pokemon[i].life)+"\t\n")			

					self.client[i].send("AFF\thurt itself in its confusion !\t\n")
					self.client[1-i].send("EAFF\thurt itself in its confusion !\t\n")
					return False
			else:
				self.client[i].affected = ""
				self.client[1-i].send("HIE\tSTOP\t\n")
				self.client[i].send("ATE\tSTOP\t\n")				
				self.client[i].send("AFF\tis not confused anymore !\t\n")
				self.client[1-i].send("EAFF\tis not confused anymore !\t\n")
				
		# Compute attack
		att 		= 	self.pokemon[i].attacks[int(self.attack[i]) - 1]
		success 	= 	Pokemon.success(self.pokemon[i],self.pokemon[1-i],att)
		critical 	= 	Pokemon.critical(self.pokemon[i])
		eff 		=	Types.get_eff(self.pokemon[1-i].type,att.type)
		self.pokemon[1-i].hit(self.pokemon[i],self.pokemon[1-i],att,success,critical,eff)

		if(self.pokemon[i].attacks[self.attack[i]].name == "Explosion" or self.pokemon[i].attacks[self.attack[i]].name == "Selfdestruct" ):
			self.pokemon[i].life = 0
			
		# Update lives
		self.client[i].send("EUPD\t"+ str(self.pokemon[1-i].life)+"\t\n")			
		self.client[1-i].send("UPD\t"+ str(self.pokemon[1-i].life)+"\t\n")

		# Send attack infos
		self.client[1-i].send("ATT\t" + att.name + "\t" + str(success) + "\t" + str(critical) + "\t" + str(eff)+"\t\n")
		self.client[i].send("HIT\t" + att.name + "\t" + str(success) + "\t" + str(critical) + "\t" + str(eff)+"\t\n")
		
		# Check post effect
		if(self.pokemon[1-i].apply_effect(att)):
			self.client[1-i].send("HIE\t"+self.pokemon[1-i].affected+"\t\n")
			self.client[i].send("ATE\t"+self.pokemon[1-i].affected+"\t\n")
		
		return (success == 1)
	
	def handle_post_effects(self,i):
		if(self.pokemon[i].affected == "Poisoned"):
			conf = Attack("poison","none",40,100)
			self.pokemon[i].hit(self.pokemon[i],self.pokemon[i],conf,1,0,1)				
		
			# Update lives
			self.client[i].say("UPD\t"+ str(self.pokemon[i].life)+"\t\n")
			self.client[1-i].say("EUPD\t"+ str(self.pokemon[i].life)+"\t\n")			

			self.client[i].send("AFF\tis hurt by the poison !\t\n")
			self.client[1-i].send("EAFF\tis hurt by the poison !\t\n")

		if(self.pokemon[i].affected == "Burning"):
			conf = Attack("burn","Fire",40,100)
			self.pokemon[i].hit(self.pokemon[i],self.pokemon[i],conf,1,0,1)				

			# Update lives
			self.client[i].say("UPD\t"+ str(self.pokemon[i].life)+"\t\n")
			self.client[1-i].say("EUPD\t"+ str(self.pokemon[i].life)+"\t\n")			

			self.client[i].send("AFF\tburns !\t\n")
			self.client[1-i].send("EAFF\tburns !\t\n")
			
	def get_order(self):
		if(self.pokemon[0].speed > self.pokemon[1].speed):
			order = [0,1]
		else:
			order = [1,0]
		# Check for quick attack
		if(self.pokemon[order[1]].attacks[int(self.attack[order[1]]) -1].name == "Quick Attack" and self.pokemon[order[0]].attacks[int(self.attack[order[0]]) -1].name != "Quick Attack"):
			order = [order[1],order[0]]
		return order

class Fights():
	fights = []
	
	@classmethod
	def get_fight(self,s):
		for f in self.fights:
			if(f.client[0].socket == s or f.client[1].socket == s):
				return f
		return -1


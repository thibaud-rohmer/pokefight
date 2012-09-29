import time
import random

class Pokemon:
	
	def __init__(self):
		self.name = ""
		self.life = 10
		self.maxlife = 10
		self.level = 1
		self.attacks = []

	def __init__(self,name,life,level,attacks,front,back):
		self.name = name
		self.life = life
		self.level = level
		self.attacks = attacks
		self.maxlife = life
		self.front = front
		self.back = back

	def __repr__(self):
		return self.name + " " + str(self.level) + " " + str(self.life)+ " " + str(self.maxlife) + " " + self.front + " " + self.back

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
		print self.attacks[0].get() + "\t\t\t\t" + self.attacks[1].get()
		print self.attacks[2].get() + "\t\t\t\t" + self.attacks[3].get()
	
	def hit(self,h):
		self.life = self.life - h

	def disp_front(self):
		print self.name + " lvl." + str(self.level)
		print self.get_life() + "\t\t\t\t\t" + self.front
		print ""
		print ""
		print ""

	def disp_back(self):
		a = "\t"
		for i in range(5):
			a = a + "\t"
		print a + self.name + " lvl." + str(self.level)
		print self.back + a + self.get_life()
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
		s = self.name + "\t"  + str(self.maxlife) + "\t" +str(self.level) 
		for i in range(4):
			s = s + "\t" + self.attacks[i].name + "\t" + str(self.attacks[i].strength)
		s = s + "\t" + self.front + "\t" + self.back
		return s

class Attack:
	
	def __init__(self,name,strength):
		self.name = name
		self.strength = strength

	def aff(self):
		print self.get()

	def get(self):
		return self.name + "\t\t" + str(self.strength)
		
		
class Fight:
	
	def __init__(self,p1,p2):
		turn = 0
		while( p1.life > 0 and p2.life > 0 ):
			clear()
			if( turn == 0 ):
				p2.disp_front()
				p1.disp_back()
				at = p1.ask_attak()
				if(p1.disp_attacking(at)):
					p2.hit(at.strength)
			else:
				p1.disp_front()
				p2.disp_back()
				at = p2.ask_attak()
				if(p2.disp_attacking(at)):
					p1.hit(at.strength)
			turn = 1-turn

		if(p1.life == 0):
			self.winner = p2
		else:
			self.winner = p1
		
		self.disp_winner()

	def disp_winner(self):
		clear()
		for i in range(3):
			print ""
		a = "\t"
		for i in range(2):
			a = a + "\t"
		print a + self.winner.name + " wins !"
		for i in range(5):
			print ""
		try:
			input()
		except:
			pass
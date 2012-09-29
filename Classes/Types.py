class Types:
	
	normal = { 
				"normal": 1 ,
				"fight":  2 ,
				"flying": 1 ,
				"poison": 1 ,
				"ground": 1 ,
				"rock":   1 ,
				"bug":    1 ,
				"ghost":  0 ,
				"fire":   1 ,
				"water":  1 ,
				"grass":  1 ,
				"electr":  1 ,
				"psychic":1 ,
				"ice":    1 ,
				"dragon": 1 ,
			}

	
	fight = { 
				"normal": 1 ,
				"fight":  1 ,
				"flying": 2 ,
				"poison": 1 ,
				"ground": 1 ,
				"rock":   0.5 ,
				"bug":    0.5 ,
				"ghost":  1 ,
				"fire":   1 ,
				"water":  1 ,
				"grass":  1 ,
				"electr":  1 ,
				"psychic":2 ,
				"ice":    1 ,
				"dragon": 1 ,
			}

	flying = { 
				"normal": 1 ,
				"fight":  0.5 ,
				"flying": 1 ,
				"poison": 1 ,
				"ground": 0 ,
				"rock":   2 ,
				"bug":    0.5 ,
				"ghost":  1 ,
				"fire":   1 ,
				"water":  1 ,
				"grass":  0.5 ,
				"electr":  2 ,
				"psychic":1 ,
				"ice":    2 ,
				"dragon": 1 ,
			}

	poison = { 
			"normal": 1 ,
			"fight":  0.5 ,
			"flying": 1 ,
			"poison": 0.5 ,
			"ground": 2 ,
			"rock":   1 ,
			"bug":    2 ,
			"ghost":  1 ,
			"fire":   1 ,
			"water":  1 ,
			"grass":  0.5 ,
			"electr":  1 ,
			"psychic":2 ,
			"ice":    1 ,
			"dragon": 1 ,
		}
	

	ground = { 
				"normal": 1 ,
				"fight":  1 ,
				"flying": 1 ,
				"poison": 0.5 ,
				"ground": 1 ,
				"rock":   0.5 ,
				"bug":    1 ,
				"ghost":  1 ,
				"fire":   1 ,
				"water":  2 ,
				"grass":  2 ,
				"electr":  0 ,
				"psychic":1 ,
				"ice":    2 ,
				"dragon": 1 ,
			}


	rock = { 
				"normal": 0.5 ,
				"fight":  2 ,
				"flying": 0.5 ,
				"poison": 0.5 ,
				"ground": 2 ,
				"rock":   1 ,
				"bug":    1 ,
				"ghost":  1 ,
				"fire":   0.5 ,
				"water":  2 ,
				"grass":  2 ,
				"electr":  1 ,
				"psychic":1 ,
				"ice":    1 ,
				"dragon": 1 ,
			}

	bug = { 
				"normal": 1 ,
				"fight":  0.5 ,
				"flying": 2 ,
				"poison": 2 ,
				"ground": 0.5 ,
				"rock":   2 ,
				"bug":    1 ,
				"ghost":  1 ,
				"fire":   2 ,
				"water":  1 ,
				"grass":  0.5 ,
				"electr":  1 ,
				"psychic":1 ,
				"ice":    1 ,
				"dragon": 1 ,
			}

	ghost = { 
			"normal": 0 ,
			"fight":  0 ,
			"flying": 1 ,
			"poison": 0.5 ,
			"ground": 1 ,
			"rock":   1 ,
			"bug":    0.5 ,
			"ghost":  2 ,
			"fire":   1 ,
			"water":  1 ,
			"grass":  1 ,
			"electr":  1 ,
			"psychic":1 ,
			"ice":    1 ,
			"dragon": 1 ,
		}
		
	fire = { 
				"normal": 1 ,
				"fight":  1 ,
				"flying": 1 ,
				"poison": 1 ,
				"ground": 2 ,
				"rock":   2 ,
				"bug":    0.5 ,
				"ghost":  1 ,
				"fire":   0.5 ,
				"water":  2 ,
				"grass":  0.5 ,
				"electr":  1 ,
				"psychic":1 ,
				"ice":    1 ,
				"dragon": 1 ,
			}


	water = { 
				"normal": 1 ,
				"fight":  1 ,
				"flying": 1 ,
				"poison": 1 ,
				"ground": 1 ,
				"rock":   1 ,
				"bug":    1 ,
				"ghost":  1 ,
				"fire":   0.5 ,
				"water":  0.5 ,
				"grass":  2 ,
				"electr":  2 ,
				"psychic":1 ,
				"ice":    0.5 ,
				"dragon": 1 ,
			}

	grass = { 
				"normal": 1 ,
				"fight":  1 ,
				"flying": 2 ,
				"poison": 2 ,
				"ground": 0.5 ,
				"rock":   1 ,
				"bug":    2 ,
				"ghost":  1 ,
				"fire":   2 ,
				"water":  0.5 ,
				"grass":  0.5 ,
				"electr":  0.5 ,
				"psychic":1 ,
				"ice":    2 ,
				"dragon": 1 ,
			}

	electr = { 
			"normal": 1 ,
			"fight":  1 ,
			"flying": 0.5 ,
			"poison": 1 ,
			"ground": 2 ,
			"rock":   1 ,
			"bug":    1 ,
			"ghost":  1 ,
			"fire":   1 ,
			"water":  1 ,
			"grass":  1 ,
			"electr":  0.5 ,
			"psychic":1 ,
			"ice":    1 ,
			"dragon": 1 ,
		}
	
	psychic = { 
			"normal": 1 ,
			"fight":  0.5 ,
			"flying": 1 ,
			"poison": 1 ,
			"ground": 1 ,
			"rock":   1 ,
			"bug":    2 ,
			"ghost":  0 ,
			"fire":   1 ,
			"water":  1 ,
			"grass":  1 ,
			"electr":  1 ,
			"psychic":0.5 ,
			"ice":    1 ,
			"dragon": 1 ,
		}
		
	ice = { 
			"normal": 1 ,
			"fight":  2 ,
			"flying": 1 ,
			"poison": 1 ,
			"ground": 1 ,
			"rock":   2 ,
			"bug":    1 ,
			"ghost":  1 ,
			"fire":   2 ,
			"water":  1 ,
			"grass":  1 ,
			"electr":  1 ,
			"psychic":1 ,
			"ice":    0.5 ,
			"dragon": 1 ,
		}
		
	dragon = { 
			"normal": 1 ,
			"fight":  1 ,
			"flying": 1 ,
			"poison": 1 ,
			"ground": 1 ,
			"rock":   1 ,
			"bug":    1 ,
			"ghost":  1 ,
			"fire":   0.5 ,
			"water":  0.5 ,
			"grass":  0.5 ,
			"electr":  0.5 ,
			"psychic":1 ,
			"ice":    2 ,
			"dragon": 2 ,
		}
		
	@classmethod
	def main(cls):
		Types.t = {}
		Types.t['normal']   = Types.normal
		Types.t['fight']	= Types.fight
		Types.t['flying']	= Types.flying
		Types.t['poison']	= Types.poison
		Types.t['ground']	= Types.ground
		Types.t['rock']		= Types.rock 
		Types.t['bug']		= Types.bug  
		Types.t['ghost']	= Types.ghost
		Types.t['fire']		= Types.fire 
		Types.t['water']	= Types.water
		Types.t['grass']	= Types.grass
		Types.t['electr']	= Types.electr
		Types.t['psychic']	= Types.psychic
		Types.t['ice']		= Types.ice 
		Types.t['dragon']	= Types.dragon
		
	@classmethod
	def get_eff(cls,p_type,at_type):
		return Types.t[p_type][at_type]
	

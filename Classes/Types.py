class Types:
	
	Normal = { 
				"Normal": 1 ,
				"Fight":  2 ,
				"Flying": 1 ,
				"Poison": 1 ,
				"Ground": 1 ,
				"Rock":   1 ,
				"Bug":    1 ,
				"Ghost":  0 ,
				"Fire":   1 ,
				"Water":  1 ,
				"Grass":  1 ,
				"Electr":  1 ,
				"Psychic":1 ,
				"Ice":    1 ,
				"Dragon": 1 ,
			}

	
	Fight = { 
				"Normal": 1 ,
				"Fight":  1 ,
				"Flying": 2 ,
				"Poison": 1 ,
				"Ground": 1 ,
				"Rock":   0.5 ,
				"Bug":    0.5 ,
				"Ghost":  1 ,
				"Fire":   1 ,
				"Water":  1 ,
				"Grass":  1 ,
				"Electr":  1 ,
				"Psychic":2 ,
				"Ice":    1 ,
				"Dragon": 1 ,
			}

	Flying = { 
				"Normal": 1 ,
				"Fight":  0.5 ,
				"Flying": 1 ,
				"Poison": 1 ,
				"Ground": 0 ,
				"Rock":   2 ,
				"Bug":    0.5 ,
				"Ghost":  1 ,
				"Fire":   1 ,
				"Water":  1 ,
				"Grass":  0.5 ,
				"Electr":  2 ,
				"Psychic":1 ,
				"Ice":    2 ,
				"Dragon": 1 ,
			}

	Poison = { 
			"Normal": 1 ,
			"Fight":  0.5 ,
			"Flying": 1 ,
			"Poison": 0.5 ,
			"Ground": 2 ,
			"Rock":   1 ,
			"Bug":    2 ,
			"Ghost":  1 ,
			"Fire":   1 ,
			"Water":  1 ,
			"Grass":  0.5 ,
			"Electr":  1 ,
			"Psychic":2 ,
			"Ice":    1 ,
			"Dragon": 1 ,
		}
	

	Ground = { 
				"Normal": 1 ,
				"Fight":  1 ,
				"Flying": 1 ,
				"Poison": 0.5 ,
				"Ground": 1 ,
				"Rock":   0.5 ,
				"Bug":    1 ,
				"Ghost":  1 ,
				"Fire":   1 ,
				"Water":  2 ,
				"Grass":  2 ,
				"Electr":  0 ,
				"Psychic":1 ,
				"Ice":    2 ,
				"Dragon": 1 ,
			}


	Rock = { 
				"Normal": 0.5 ,
				"Fight":  2 ,
				"Flying": 0.5 ,
				"Poison": 0.5 ,
				"Ground": 2 ,
				"Rock":   1 ,
				"Bug":    1 ,
				"Ghost":  1 ,
				"Fire":   0.5 ,
				"Water":  2 ,
				"Grass":  2 ,
				"Electr":  1 ,
				"Psychic":1 ,
				"Ice":    1 ,
				"Dragon": 1 ,
			}

	Bug = { 
				"Normal": 1 ,
				"Fight":  0.5 ,
				"Flying": 2 ,
				"Poison": 2 ,
				"Ground": 0.5 ,
				"Rock":   2 ,
				"Bug":    1 ,
				"Ghost":  1 ,
				"Fire":   2 ,
				"Water":  1 ,
				"Grass":  0.5 ,
				"Electr":  1 ,
				"Psychic":1 ,
				"Ice":    1 ,
				"Dragon": 1 ,
			}

	Ghost = { 
			"Normal": 0 ,
			"Fight":  0 ,
			"Flying": 1 ,
			"Poison": 0.5 ,
			"Ground": 1 ,
			"Rock":   1 ,
			"Bug":    0.5 ,
			"Ghost":  2 ,
			"Fire":   1 ,
			"Water":  1 ,
			"Grass":  1 ,
			"Electr":  1 ,
			"Psychic":1 ,
			"Ice":    1 ,
			"Dragon": 1 ,
		}
		
	Fire = { 
				"Normal": 1 ,
				"Fight":  1 ,
				"Flying": 1 ,
				"Poison": 1 ,
				"Ground": 2 ,
				"Rock":   2 ,
				"Bug":    0.5 ,
				"Ghost":  1 ,
				"Fire":   0.5 ,
				"Water":  2 ,
				"Grass":  0.5 ,
				"Electr":  1 ,
				"Psychic":1 ,
				"Ice":    1 ,
				"Dragon": 1 ,
			}


	Water = { 
				"Normal": 1 ,
				"Fight":  1 ,
				"Flying": 1 ,
				"Poison": 1 ,
				"Ground": 1 ,
				"Rock":   1 ,
				"Bug":    1 ,
				"Ghost":  1 ,
				"Fire":   0.5 ,
				"Water":  0.5 ,
				"Grass":  2 ,
				"Electr":  2 ,
				"Psychic":1 ,
				"Ice":    0.5 ,
				"Dragon": 1 ,
			}

	Grass = { 
				"Normal": 1 ,
				"Fight":  1 ,
				"Flying": 2 ,
				"Poison": 2 ,
				"Ground": 0.5 ,
				"Rock":   1 ,
				"Bug":    2 ,
				"Ghost":  1 ,
				"Fire":   2 ,
				"Water":  0.5 ,
				"Grass":  0.5 ,
				"Electr":  0.5 ,
				"Psychic":1 ,
				"Ice":    2 ,
				"Dragon": 1 ,
			}

	Electr = { 
			"Normal": 1 ,
			"Fight":  1 ,
			"Flying": 0.5 ,
			"Poison": 1 ,
			"Ground": 2 ,
			"Rock":   1 ,
			"Bug":    1 ,
			"Ghost":  1 ,
			"Fire":   1 ,
			"Water":  1 ,
			"Grass":  1 ,
			"Electr":  0.5 ,
			"Psychic":1 ,
			"Ice":    1 ,
			"Dragon": 1 ,
		}
	
	Psychic = { 
			"Normal": 1 ,
			"Fight":  0.5 ,
			"Flying": 1 ,
			"Poison": 1 ,
			"Ground": 1 ,
			"Rock":   1 ,
			"Bug":    2 ,
			"Ghost":  0 ,
			"Fire":   1 ,
			"Water":  1 ,
			"Grass":  1 ,
			"Electr":  1 ,
			"Psychic":0.5 ,
			"Ice":    1 ,
			"Dragon": 1 ,
		}
		
	Ice = { 
			"Normal": 1 ,
			"Fight":  2 ,
			"Flying": 1 ,
			"Poison": 1 ,
			"Ground": 1 ,
			"Rock":   2 ,
			"Bug":    1 ,
			"Ghost":  1 ,
			"Fire":   2 ,
			"Water":  1 ,
			"Grass":  1 ,
			"Electr":  1 ,
			"Psychic":1 ,
			"Ice":    0.5 ,
			"Dragon": 1 ,
		}
		
	Dragon = { 
			"Normal": 1 ,
			"Fight":  1 ,
			"Flying": 1 ,
			"Poison": 1 ,
			"Ground": 1 ,
			"Rock":   1 ,
			"Bug":    1 ,
			"Ghost":  1 ,
			"Fire":   0.5 ,
			"Water":  0.5 ,
			"Grass":  0.5 ,
			"Electr":  0.5 ,
			"Psychic":1 ,
			"Ice":    2 ,
			"Dragon": 2 ,
		}
		
	@classmethod
	def main(cls):
		Types.t = {}
		Types.t['Normal']   = Types.Normal
		Types.t['Fight']	= Types.Fight
		Types.t['Flying']	= Types.Flying
		Types.t['Poison']	= Types.Poison
		Types.t['Ground']	= Types.Ground
		Types.t['Rock']		= Types.Rock 
		Types.t['Bug']		= Types.Bug  
		Types.t['Ghost']	= Types.Ghost
		Types.t['Fire']		= Types.Fire 
		Types.t['Water']	= Types.Water
		Types.t['Grass']	= Types.Grass
		Types.t['Electr']	= Types.Electr
		Types.t['Psychic']	= Types.Psychic
		Types.t['Ice']		= Types.Ice 
		Types.t['Dragon']	= Types.Dragon
		
	@classmethod
	def get_eff(cls,p_type,at_type):
		print "get_eff"
		print p_type
		print at_type
		return Types.t[p_type][at_type]
	

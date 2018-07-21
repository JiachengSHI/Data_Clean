from Check import Check

class Patient:
	def __init__(self, data):
		all_d = data.split('\t', 1)
		self.id = all_d[0]
		self.first_treat = False
		self.treament_line = False
		self.Check_list = [Check(all_d[1])]

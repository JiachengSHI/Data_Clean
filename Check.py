class Check:
	def __init__(self, record):
		#print record
		#if record != None and record != "":
		r = record.split('\t')
		self.EGFR = r[0]
		self.ALK = r[1]
		self.Wrose = r[2]
		self.WroseLabel = r[3]
		self.Treat = r[4]
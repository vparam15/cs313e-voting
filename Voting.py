class Candidate:
	def __init__ (self, name, num):
		self.name = name
		self.num = num
		self.count = 0
		self.ballots = []

	def getname (self):
		return self.name

	def getcount (self):
		return self.count

	def increment (self, bal):
		self.count += 1
		self.ballots.append (bal.choices)

class Ballot:
	def __init__ (self, choices):
		self.choices = choices

	def getchoice (self, run = 0):
		x = int(self.choices[run])
		run += 1
		return x

def voting_read():
	r = open('/v/filer4b/v35q001/vparam/cs313e/projects/cs313e-voting/RunVoting.in', 'r')
	# while (True):
	# 	line = r.readline()
	# 	if not line:
	# 		break
	# 	totalcases = int(line)
	# 	for case in range (totalcases + 1):
	totcases = int(r.readline())
	r.readline()
	totcandidates = int(r.readline())
	clist = []
	for i in range (totcandidates): 
		clist.append(Candidate(r.readline(), i + 1))
	while (True):
		line = r.readline()
		if (line == ''):
			break
		ballot = Ballot(line.split())
		choice1 = ballot.getchoice()
		for c in clist:
			if (choice1 == c.num):
				c.increment(ballot)
	for c in clist:
		print (c.name, c.num, c.count, c.ballots)

voting_read()
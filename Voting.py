import math
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

def find_winner (clist, majority):
	for c in clist:
		if c.count >= majority:
			print(c.name)
			break

def find_tie (clist, tie_num):
	all_tied = True
	for c in clist:
		if c.count != tie_num:
			all_tied == False
	if all_tied == True:
		print ("No winner")

def voting_read():
	r = open('/v/filer4b/v35q001/vparam/cs313e/projects/cs313e-voting/RunVoting.in', 'r')
	while (True):
		line = r.readline()
		if not line:
			break
		totelections = int(line)
		r.readline()
		for election in range (totelections):
			numBallots = -1
			totcandidates = int(r.readline())
			clist = []
			for i in range (totcandidates): 
				clist.append(Candidate(r.readline(), i + 1))
			while (True):
				numBallots += 1
				line = r.readline()
				if len(line) <= 1:
					break
				ballot = Ballot(line.split())
				choice1 = ballot.getchoice()
				for c in clist:
					if (choice1 == c.num):
						c.increment(ballot)
			majority = math.ceil(numBallots / 2)
			tie_num = numBallots/totcandidates
			find_winner (clist, majority)
			find_tie (clist, tie_num)

voting_read()
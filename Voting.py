import math

class Candidate:
	def __init__ (self, name, num):
		self.name = name
		self.num = num
		self.count = 0
		self.ballots = []
		self.running = True

	def getname (self):
		return self.name

	def getcount (self):
		return self.count

	def increment (self, b): 
		self.count += 1
		self.ballots.append (b)

class Ballot:
	def __init__ (self, choices):
		self.choices = choices
		self.marker = 0

	def getchoice (self):
		x = int(self.choices[self.marker])
		self.marker += 1
		return x

def find_winner (clist, majority):
	for c in clist:
		if c.count > majority:
			print(c.name)
	global done
	done = True

def find_tie (clist, tie_num):
	all_tied = True
	for c in clist:
		if c.count == tie_num:
			pass
		else:
			all_tied = False
	if all_tied == True:
		for c in clist:
			print (c.name)
	global done
	done = True

def voting_solve (clist):
	max_count = 0
	for c in clist:
		if c.count >= max_count:
			max_count = c.count
		else:
			c.running = False
	for c in clist:
		if c.running is False:
			for b in c.ballots:
				transferred = False
				while not transferred:
					next_choice = b.getchoice()
					for c in clist:
						if c.running is True:
							if next_choice == c.num:
								c.increment(b)
								transferred = True

def voting_read (r, w):
	r = open('/v/filer4b/v35q001/vparam/cs313e/projects/cs313e-voting/cs313e-voting/RunVoting.in', 'r')

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
			done = False
			while not done:
				find_winner (clist, majority)
				if done == True:
					break
				find_tie (clist, tie_num)
				if done == True:
					break
				voting_solve (clist)

voting_read()
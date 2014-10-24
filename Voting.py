import math

class Candidate:
	def __init__ (self, name, num):
		self.name = name
		self.num = num
		self.count = 0
		self.ballots = []
		self.running = True

	def getinfo (self):
		return (self.name, self.num, self.count, self.ballots, self.running)

	def increment (self, b):
		self.count += 1
		self.ballots.append (b)

class Ballot:
	def __init__ (self, choices):
		self.choices = choices
		self.marker = 0

	def getchoice (self):
		x = int(self.choices[self.marker])
		return x

	def getinfo (self):
		return (self.choices, self.marker)

def find_winner (clist, numBallots):
	tie = numBallots // 2
	max_count = 1
	max_clist = []
	for c in clist:
		if c.count >= max_count:
			max_count = c.count
	for c in clist:
		if c.count == max_count:
			max_clist.append(c)
	if max_count > tie:
		for max_c in max_clist:
			print(max_c.name)
		return True
	return False

def find_tie (clist, numBallots):
	tie = numBallots / len(clist)
	all_tied = True
	for c in clist:
		if c.count == tie:
			pass
		else:
			all_tied = False
	tie_print = ''
	if all_tied == True:
		for c in clist:
			tie_print += c.name
		print(tie_print)
		return True
	return False

def find_losers (clist, numBallots):
	max_count = 1
	loser_list = []
	for c in clist:
		if c.count >= max_count:
			max_count = c.count
		else:
			loser_list.append (c)
	return loser_list

def empty_losers (clist, loser_list):
	removelist = []
	for c in clist:
		if c in loser_list:
			loser = c
			c.running = False
			removelist.append (loser)

	for c in removelist:
		reassign (c, clist)
		clist.remove(c)

def reassign (loser, clist):
	found = False
	new_c = None
	for ballot in loser.ballots:
		while not found:
			ballot.marker += 1
			if ballot.marker >= len(ballot.choices):
				break
			for c in clist:
				if (int(ballot.choices[ballot.marker]) == int(c.num)) and c.running:
					found = True
					new_c = c
					break
		new_c.increment(ballot)

def voting_solve (r, w):
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

			while True:
				found_winner = find_winner (clist, numBallots)
				if found_winner:
					break
				found_tie = find_tie (clist, numBallots)
				if found_tie:
					break
				loser_list = find_losers(clist, numBallots)
				empty_losers (clist, loser_list)
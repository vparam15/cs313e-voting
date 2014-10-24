class Candidate: 
	def __init__ (self, name, num): # initialize Candidate class with name, number, count of ballots, list of ballots, and boolean describing whether they are still running or not
		self.name = name
		self.num = num
		self.count = 0
		self.ballots = []
		self.running = True

	def getinfo (self): # return all Candidate info
		return (self.name, self.num, self.count, self.ballots, self.running)

	def increment (self, b): # Increase the ballot count by 1 and add a ballot to the ballot list
		self.count += 1
		self.ballots.append (b)

class Ballot:
	def __init__ (self, choices): # Initialize Ballot class with list of choices and a marker
		self.choices = choices
		self.marker = 0

	def getchoice (self): # return the ballot choice pointed to by the marker
		x = int(self.choices[self.marker])
		return x

	def getinfo (self): # Return all Ballot info
		return (self.choices, self.marker)

# Finds a clear winner (greater than 50% of votes) and if found, writes to output
def find_winner (clist, numBallots, w):
	outfile = (w)
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
			outfile.write(max_c.name)
			outfile.write("\n")
		return True
	return False

# Finds an "all-way" tie and if found, writes to output
def find_tie (clist, numBallots, w):
	outfile = (w)
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
		outfile.write(tie_print)
		outfile.write("\n")
		return True
	return False

# Finds all losers (less than the maximum number of votes earned by candidate(s)) and returns them in a list
def find_losers (clist, numBallots):
	max_count = 1
	loser_list = []
	for c in clist:
		if c.count >= max_count:
			max_count = c.count
		else:
			loser_list.append (c)
	return loser_list

# Removes all losers from the overall candidate list
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

# Reassigns the ballots of the losers, based on subsequent choices, to another candidate
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

# Reads input, populates candidate list with first ballots, and runs tests one-by-one
def voting_solve (r, w):
	# Reads input by election, then by candidate, then by ballot
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
			
			# Populates candidate list with first ballots of each candidate
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

			# Runs tests for clear winner, clear tie, and reassignment of losers one-by-one
			while True:
				found_winner = find_winner (clist, numBallots, w)
				if found_winner:
					break
				found_tie = find_tie (clist, numBallots, w)
				if found_tie:
					break
				loser_list = find_losers(clist, numBallots)
				empty_losers (clist, loser_list)
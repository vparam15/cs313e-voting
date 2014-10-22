def voting_read():
	r = open('/v/filer4b/v35q001/vparam/cs313e/projects/cs313e-voting/RunVoting.in', 'r')
	totalcases = int(r.readline())
	for case in range (totalcases + 1):
		r.readline()
		candidates = int(r.readline())
		dictionary = {}
		for i in range (candidates): 
			s = r.readline()
			dictionary[s[:-1]] = 0
		print(dictionary)
		ballots = []
		while (True):
			line = r.readline()
			if not line:
				break
			ballot = line.split()
			print(ballot)


voting_read()
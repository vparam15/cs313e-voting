def voting_read():
	r = open("filename")
	totalcases = int(r.readline())
	for case in range (totalcases + 1):
		r.readline()
		candidates = int(r.readline())
		dictionary = {}
		for i in range (candidates):
			s = r.readline()
			dictionary[s[:-1]] = 0 
		ballots = []
		while (r.readline is not '/n'): 
			ballot = r.readline().split()
			print (ballot)

voting_read()
def voting_read(r1):
	r = open(r1, 'r')
	numcases = r.readline()
	print(numcases)

r1 = firsttest.txt
voting_read(r1)
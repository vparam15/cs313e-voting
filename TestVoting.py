from io import StringIO
from unittest import main, TestCase

from Voting import Candidate, Ballot, voting_solve, find_winner, find_tie, find_losers, empty_losers, reassign

# voting_solve implements all of the other functions, so our unit tests only test it

class TestVoting (TestCase):

    # ----
    # class Candidate tests
    # ----

	def testCinit1 (self):
		c = Candidate("Barack Obama", 1)
		self.assertEqual (c.name, "Barack Obama")

	def testCinit2 (self):
		c = Candidate("Mitt Romney", 2)
		self.assertEqual(c.num, 2)

	def testCinit3 (self):
		c = Candidate("Apple", 3)
		self.assertEqual(c.count, 0)
		self.assertEqual(c.ballots, [])
		self.assertEqual(c.running, True)

	def testCgetinfo1 (self):
		c = Candidate("Barack Obama", 1)
		c.count = 1
		c.ballots.append(1)
		c.running = False
		self.assertEqual(c.getinfo(), ('Barack Obama', 1, 1, [1], False))

	def testCgetinfo2 (self):
		c = Candidate("Mitt Romney", 1)
		c.count = 1
		c.ballots.append([1, 2, 3])
		self.assertEqual(c.getinfo(), ('Mitt Romney', 1, 1, [[1, 2, 3]], True))

	def testCgetinfo3 (self):
		c = Candidate("Glenn Downing", 500)
		c.count = 2
		c.ballots.append([1, 2, 3])
		c.ballots.append([1, 3, 2])
		self.assertEqual(c.getinfo(), ('Glenn Downing', 500, 2, [[1, 2, 3], [1, 3, 2]], True))

	def testC_increment1 (self):
		c = Candidate("Prateek", 1)
		c.increment([1, 2])
		self.assertEqual(c.count, 1)
		self.assertEqual(c.ballots, [[1, 2]])

	def testC_increment2 (self):
		c = Candidate("Fiona", 1)
		c.increment([1, 2, 3])
		self.assertEqual(c.count, 1)
		self.assertEqual(c.ballots, [[1, 2, 3]])

	def testC_increment3 (self):
		c = Candidate("Josh", 1)
		c.increment([1, 2, 3])
		c.increment([1, 2, 3])
		c.increment([1, 3, 2])
		self.assertEqual(c.count, 3)
		self.assertEqual(c.ballots, [[1, 2, 3], [1, 2, 3], [1, 3, 2]])

    # ----
    # class Ballot tests
    # ----

	def testB_init1 (self):
		b = Ballot([1, 2, 3])
		self.assertEqual(b.choices, [1, 2, 3])
		self.assertEqual(b.marker, 0)
		self.assertEqual(b.choices[b.marker], 1)

	def testB_init2 (self):
		b = Ballot([1, 2, 3])
		b.marker += 1
		self.assertEqual(b.choices, [1, 2, 3])
		self.assertEqual(b.marker, 1)
		self.assertEqual(b.choices[b.marker], 2)

	def testB_init3 (self):
		b = Ballot([1, 2, 3])
		b.marker += 2
		self.assertEqual(b.choices, [1, 2, 3])
		self.assertEqual(b.marker, 2)
		self.assertEqual(b.choices[b.marker], 3)

	def testB_getchoice1 (self):
		b = Ballot([1, 2, 3])
		self.assertEqual(b.getchoice(), 1)

	def testB_getchoice2 (self):
		b = Ballot([1, 2, 3])
		b.marker += 1
		self.assertEqual(b.getchoice(), 2)

	def testB_getchoice3 (self):
		b = Ballot([1, 2, 3])
		b.marker += 2
		self.assertEqual(b.getchoice(), 3)

	def testB_getinfo1 (self):
		b = Ballot([1])
		self.assertEqual(b.getinfo(), ([1], 0))

	def testB_getinfo2 (self):
		b = Ballot([1, 10, 100, 1000])
		b.marker += 2
		self.assertEqual(b.getinfo(), ([1, 10, 100, 1000], 2))

	def testB_getinfo3 (self):
		b = Ballot([1, 2, 3])
		self.assertEqual(b.getinfo(), ([1, 2, 3], 0))

	# ----
	# voting_solve
	# ----

	def test_solve_1 (self): 
		r = StringIO ("1\n \n2\nRed\nGreen\n1 2\n2 1\n1 2\n1 2")
		w = StringIO()
		voting_solve(r, w)
		self.assertEqual (w.getvalue(), "Red\n\n")

	def test_solve_2 (self): 
		r = StringIO ("1\n \n3\nRed\nGreen\nBlue\n3 2 1\n3 1 2\n2 3 1\n3 1 2\n")
		w = StringIO()
		voting_solve(r,w)
		self.assertEqual (w.getvalue(), "Blue\n\n")

	def test_solve_3 (self): 
		r = StringIO ("1\n \n3\nRed\nGreen\nBlue\n1 2 3\n2 1 3\n2 3 1\n3 1 2\n1 3 2")
		w = StringIO()
		voting_solve(r,w)
		self.assertEqual (w.getvalue(), "Red\n\n")

	def test_solve_4 (self): 
		r = StringIO ("2\n \n3\nRed\nGreen\nBlue\n1 2 3 \n2 1 3 \n2 3 1 \n3 1 2 \n1 3 2 \n\n2\nJohn\nJake\n1 2\n2 1\n1 2")
		w = StringIO()
		voting_solve(r,w)
		self.assertEqual (w.getvalue(), "Red\n\nJohn\n\n")

	def test_solve_5 (self): 
		r = StringIO ("1\n \n2\nRed\nGreen\n1 2\n2 1\n1 2\n2 1")
		w = StringIO()
		voting_solve(r,w)
		self.assertEqual (w.getvalue(), "Red\nGreen\n\n")

	def test_solve_6 (self): 
		r = StringIO ("1\n \n2\nRed\nGreen\n1 2\n2 1\n1 2\n1 2")
		w = StringIO()
		voting_solve(r,w)
		self.assertEqual (w.getvalue(), "Red\n\n")

	def test_solve_7 (self): 
		r = StringIO ("1\n \n3\nRed\nGreen\nBlue\n1 2 3\n2 1 3\n2 3 1\n3 1 2\n2 1 3")
		w = StringIO()
		voting_solve(r,w)
		self.assertEqual (w.getvalue(), "Green\n\n")

	def test_solve_8 (self): 
		r = StringIO ("1\n \n3\nRed\nGreen\nBlue\n1 2 3\n2 1 3\n2 3 1\n3 1 2\n1 3 2")
		w = StringIO()
		voting_solve(r,w)
		self.assertEqual (w.getvalue(), "Red\n\n")

	def test_solve_9 (self): 
		r = StringIO ("2\n \n3\nRed\nGreen\nBlue\n1 2 3 \n3 1 2 \n2 3 1 \n3 1 2 \n1 3 2 \n\n2\nJohn\nJake\n1 2\n2 1\n1 2")
		w = StringIO()
		voting_solve(r,w)
		self.assertEqual (w.getvalue(), "Blue\n\nJohn\n\n")

	def test_solve_10 (self): 
		r = StringIO ("1\n \n2\nRed\nGreen\n1 2\n2 1\n1 2\n2 1")
		w = StringIO()
		voting_solve(r,w)
		self.assertEqual (w.getvalue(), "Red\nGreen\n\n")

	def test_solve_11 (self): 
		r = StringIO ("1\n \n2\nRed\nGreen\n1 2\n1 2\n2 1")
		w = StringIO()
		voting_solve(r,w)
		self.assertEqual (w.getvalue(), "Red\n\n")

	def test_solve_12 (self): 
		r = StringIO ("1\n \n2\nRed\nGreen\n2 1\n1 2\n2 1")
		w = StringIO()
		voting_solve(r,w)
		self.assertEqual (w.getvalue(), "Green\n\n")

	def test_solve_13 (self): 
		r = StringIO ("1\n \n2\nObama\nRomney\n2 1\n1 2\n2 1")
		w = StringIO()
		voting_solve(r,w)
		self.assertEqual (w.getvalue(), "Romney\n\n")

	def test_solve_14 (self): 
		r = StringIO ("2\n \n3\nRed\nGreen\nBlue\n1 2 3\n2 1 3\n2 3 1\n3 1 2\n1 3 2\n\n2\nJohn\nJake\n2 1\n2 1\n2 1")
		w = StringIO()
		voting_solve(r,w)
		self.assertEqual (w.getvalue(), "Red\n\nJake\n\n")

	def test_solve_15 (self): 
		r = StringIO ("1\n \n2\nRed\nGreen\n2 1\n2 1\n2 1\n1 2")
		w = StringIO()
		voting_solve(r, w)
		self.assertEqual (w.getvalue(), "Green\n\n")

	def test_solve_16 (self): 
		r = StringIO ("1\n \n3\nRed\nGreen\nBlue\n2 3 1\n2 1 3\n2 3 1\n3 1 2\n")
		w = StringIO()
		voting_solve(r,w)
		self.assertEqual (w.getvalue(), "Green\n\n")

	def test_solve_17 (self):
		r = StringIO ("1\n\n3\nWashington\nAdams\nJefferson\n1 2 3\n2 3 1\n3 1 2")
		w = StringIO()
		voting_solve(r, w)
		self.assertEqual (w.getvalue(), "Washington\nAdams\nJefferson\n\n")

	def test_solve_18 (self):
		r = StringIO ("1\n \n3\nWashington\nAdams\nJefferson\n1 2 3\n1 2 3\n3 1 2\n3 2 1")
		w = StringIO()
		voting_solve(r, w)
		self.assertEqual (w.getvalue(), "Washington\nJefferson\n\n")

main()
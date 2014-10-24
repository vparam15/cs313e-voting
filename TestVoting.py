from io import StringIO
from unittest import main, TestCase

from Voting import voting_solve, find_winner, find_tie, find_losers, empty_losers, reassign

# voting_solve implements all of the other functions, so our unit tests only test it

class TestVoting (TestCase): 

	def test_solve_1 (self): 
		r = StringIO ("1\n \n2\nRed\nGreen\n1 2\n2 1\n1 2\n1 2")
		w = StringIO()
		voting_solve(r,None) > w 
		self.assertEqual (w, "Red")

	# def test_solve_2 (self): 
	# 	r = StringIO ("1\n \n3\nRed\nGreen\nBlue\n1 2 3\n2 1 3\n2 3 1\n3 1 2\n")
	# 	w = StringIO()
	# 	voting_solve(r,w)
	# 	self.assertEqual (w.getvalue(), "Green")

	# def test_solve_3 (self): 
	# 	r = StringIO ("1\n \n3\nRed\nGreen\nBlue\n1 2 3\n2 1 3\n2 3 1\n3 1 2\n1 3 2")
	# 	w = StringIO()
	# 	voting_solve(r,w)
	# 	self.assertEqual (w.getvalue(), "Red")

	# def test_solve_4 (self): 
	# 	r = StringIO ("2\n \n3\nRed\nGreen\nBlue\n1 2 3\n2 1 3\n2 3 1\n3 1 2\n1 3 2\n\
	# 		 \n2\nJohn\nJake\n1 2\n2 1\n1 2")
	# 	w = StringIO()
	# 	voting_solve(r,w)
	# 	self.assertEqual (w.getvalue(), "Red\n \nJohn")

	# def test_solve_5 (self): 
	# 	r = StringIO ("1\n \n2\nRed\nGreen\n1 2\n2 1\n1 2\n2 1")
	# 	w = StringIO()
	# 	voting_solve(r,w)
	# 	self.assertEqual (w.getvalue(), "Red\nGreen")

	# def test_solve_6 (self): 
	# 	r = StringIO ("1\n \n2\nRed\nGreen\n1 2\n2 1\n1 2\n1 2")
	# 	w = StringIO()
	# 	voting_solve(r,w)
	# 	self.assertEqual (w.getvalue(), "Red")

	# def test_solve_7 (self): 
	# 	r = StringIO ("1\n \n3\nRed\nGreen\nBlue\n1 2 3\n2 1 3\n2 3 1\n3 1 2\n")
	# 	w = StringIO()
	# 	voting_solve(r,w)
	# 	self.assertEqual (w.getvalue(), "Green")

	# def test_solve_8 (self): 
	# 	r = StringIO ("1\n \n3\nRed\nGreen\nBlue\n1 2 3\n2 1 3\n2 3 1\n3 1 2\n1 3 2")
	# 	w = StringIO()
	# 	voting_solve(r,w)
	# 	self.assertEqual (w.getvalue(), "Red")

	# def test_solve_9 (self): 
	# 	r = StringIO ("2\n \n3\nRed\nGreen\nBlue\n1 2 3\n2 1 3\n2 3 1\n3 1 2\n1 3 2\n\
	# 		 \n2\nJohn\nJake\n1 2\n2 1\n1 2")
	# 	w = StringIO()
	# 	voting_solve(r,w)
	# 	self.assertEqual (w.getvalue(), "Red\n \nJohn")

	# def test_solve_10 (self): 
	# 	r = StringIO ("1\n \n2\nRed\nGreen\n1 2\n2 1\n1 2\n2 1")
	# 	w = StringIO()
	# 	voting_solve(r,w)
	# 	self.assertEqual (w.getvalue(), "Red\nGreen")

	# def test_solve_11 (self): 
	# 	r = StringIO ("1\n \n2\nRed\nGreen\n1 2\n1 2\n2 1")
	# 	w = StringIO()
	# 	voting_solve(r,w)
	# 	self.assertEqual (w.getvalue(), "Red")

	# def test_solve_12 (self): 
	# 	r = StringIO ("1\n \n2\nRed\nGreen\n2 1\n1 2\n2 1")
	# 	w = StringIO()
	# 	voting_solve(r,w)
	# 	self.assertEqual (w.getvalue(), "Green")

main()
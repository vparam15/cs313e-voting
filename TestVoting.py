from io import StringIO
from unittest import main, TestCase

from Voting import voting_read, #function to read text???

class TestVoting (TestCase): 

	def test_solve_1 (self): 
		r = StringIO ("1\n""\n2\nRed\nGreen\n1 2\n2 1\n1 2\n1 2 ")
		w = StringIO()
		voting_read(r,w)
		self.assertEqual (w.getvalue(), "Red")

	def test_solve_2 (self): 
		r = StringIO ("1\n""\n3\nRed\nGreen\nBlue\n1 2 3 \n2 1\n1 2\n1 2 ")
		w = StringIO()
		voting_read(r,w)
		self.assertEqual (w.getvalue(), "")

	def test_solve_3 (self): 
		r = StringIO ("")
		w = StringIO()
		voting_read(r,w)
		self.assertEqual (w.getvalue(), "")

	def test_solve_4 (self): 
		r = StringIO ("")
		w = StringIO()
		voting_read(r,w)
		self.assertEqual (w.getvalue(), "")

	def test_solve_5 (self): 
		r = StringIO ("")
		w = StringIO()
		voting_read(r,w)
		self.assertEqual (w.getvalue(), "")


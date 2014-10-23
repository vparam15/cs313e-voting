# -------
# imports
# -------
import sys
import json

from Voting import voting_read, voting_solve, find_winner, find_tie
# ----
# main
# ----
voting_read(sys.stdin, sys.stdout)
#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  plays = ['rock', 'paper','scissors']
  answer = []

  def helper(current_round, outcome=[]):
    if current_round == 0:
        answer.append(outcome)
        return

    for play in plays:
      helper(current_round-1, outcome + [play])

  helper(n, [])
  return answer




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
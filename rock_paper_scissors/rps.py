#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    if n <= 0:
        return [[]]
    options = ['rock', 'paper', 'scissors']
    combinations = []
    if n >= 1:
        for option in options:
            for i in rock_paper_scissors(n-1):
                combinations.append([option]+i)
    return combinations

    
    
print(rock_paper_scissors(5))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
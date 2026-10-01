import sys

total, votes = sys.stdin.read().split()
a_votes = votes.count("A")
b_votes = int(total) - a_votes

if a_votes > b_votes:
    print("A")
elif b_votes > a_votes:
    print("B")
else:
    print("Tie")

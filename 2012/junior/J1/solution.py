import sys

limit, speed = map(int, sys.stdin.read().split())
over = speed - limit

if over <= 0:
    print("Congratulations, you are within the speed limit!")
elif over <= 20:
    print("You are speeding and your fine is $100.")
elif over <= 30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")

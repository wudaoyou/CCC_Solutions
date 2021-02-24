h = int(input())
M = int(input())

t = 1
A = -6*(t**4) + h*(t**3) + 2*(t**2) + t
while t < M and A > 0:
    t = t + 1
    A = -6*(t**4) + h*(t**3) + 2*(t**2) + t
if A > 0:
    print("The balloon does not touch ground in the given time.")
else:
    print("The balloon first touches ground at hour:")
    print(t)
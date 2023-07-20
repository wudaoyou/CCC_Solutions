# set up variables to hold inputs and output
p, c, f = int(input()), int(input()), 0

# check if the input amount is correct
if p >= 0 and c >= 0:
    # caculate total points earned and lost
    f = 50 * p - 10 * c
    # check if satisfied for bonus; if so, add 500 points
    if p > c:
        f += 500

# print output
print(f)
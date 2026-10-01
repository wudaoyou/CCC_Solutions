p, c = int(input()), int(input()) # number of delivers and number of collisions

f = 50 * p - 10 * c + (500 if p > c else 0) # total amount of points earned; 50 for each deliverd, -10 for each collision, bonus 500 if delieved more than collsions

print(f) # print output
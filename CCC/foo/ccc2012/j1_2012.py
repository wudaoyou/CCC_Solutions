speed_limit = int(input())
speed = int(input())
if speed - speed_limit <= 0:
    print('Congratulations, you are within the speed limit!')
elif speed - speed_limit <= 20:
    print('You are speeding and your fine is $%d.' % 100)
elif speed - speed_limit <= 30:
    print('You are speeding and your fine is $%d.' % 270)
elif speed - speed_limit > 30:
    print('You are speeding and your fine is $%d.' % 500)

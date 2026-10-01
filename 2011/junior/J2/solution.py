h = int(input())
maximum_hour = int(input())

landing_hour = 0
for hour in range(1, maximum_hour + 1):
    altitude = -6 * hour**4 + h * hour**3 + 2 * hour**2 + hour
    if altitude <= 0:
        landing_hour = hour
        break

if landing_hour == 0:
    print("The balloon does not touch ground in the given time.")
else:
    print("The balloon first touches ground at hour:")
    print(landing_hour)

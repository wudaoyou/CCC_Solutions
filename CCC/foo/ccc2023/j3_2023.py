day = {1:0, 2:0, 3:0, 4:0, 5:0} # days and people that will come on the day
attend = "" # wilingness of attending

# use loop to find out how many people are coming
for t in range(int(input())):
    attend = input() # let the person enter if coming or not from day 1 ro 5
    # check whether the person is coming or not
    for i in range(len(attend)):
        # if the person is coming on day i, the amount of people coming on day i add 1
        if attend[i] == "Y":
            day[i+1] += 1

multi_days = [] # days that may have same amount of people coming that are the most
d = list(day.values())
mX = max(d) # find the day with the max people coming

# find out if there are multiples days that have the same amount of people willing to come
for t2 in range(5):
    # if the people coming on day t2 equals to the max amount, add day t2 to multi-days list
    if d[t2] == mX:
        multi_days.append(str(t2+1))
        
# print output of days based on if there are multiple days that have same amount of people willing to come
if len(multi_days) == 1:
    print(multi_days[0])  # if there's only 1 day, print the day that most people are willing to come
else:
    print(",".join(multi_days)) # print all the days that most people are willing to come

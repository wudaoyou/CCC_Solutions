time_24 = int(input("Enter the time: "))
hours = time_24 // 100
minutes = time_24 % 100
am_pm = "am"
if hours == 12:
    am_pm = "pm"
if hours % 12 == 0:
    hours = 12
elif hours % 12 != hours:
    hours = hours % 12
    am_pm = "pm"

if minutes < 10:
    min_str = "0" + str(minutes)
else:
    min_str = str(minutes)

time_12 = str(hours) + ":" + min_str + am_pm
print("the currnet time is :" + time_12)

# list includes pepper name and SHU
shu_list = {"Poblano":1500, 
            "Mirasol":6000, 
            "Serrano":15500, 
            "Cayenne":40000, 
            "Thai":75000, 
            "Habanero":125000}
total_shu = 0 # sum of the shu

# find out the total shu
for t in range(int(input())):
    total_shu += shu_list[input()]

# print output
print(total_shu)

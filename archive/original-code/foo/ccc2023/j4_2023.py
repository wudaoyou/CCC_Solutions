c = int(input()) # number of columns

r1 = str(input()) # top row that will contain c amount of value
r2 = str(input()) # bot row that will contain c amount of value

# remove spaces (replace space with empty)
r1 = r1.replace(" ","")
r2 = r2.replace(" ","")

tiles = [r1, r2] # colors of the tiles
mN = 0 # min amount of tape needed

# for looping through each tile
for i in range(len(tiles)):
    for j in range(len(tiles)):
        # if the tile is black (wet), 3 meters of tape is needed
        if tiles[i][j] == "i":
            mN += 3
            # if the left or right tile to the previous one is also wet, we use 2 meters less tape
            if j > 0 and tiles[i][j-1] == "1":
                mN -=2
            # if the below or above tile is also wet, we use 2 meters less tape
            if i == 0 and tiles[i+1][j] == "1" and j % 2 == 0:
                mN -=2

print(mN) # print output


w = input() # word that will be searched in the grid
r = int(input()) # number of rows in the grid
c = int(input()) # number of cols in the grid

grid = [] # word grid
# add letters that we input into the grid
for i in range(r):
    grid.append(input().split())
    
h = 0 # number of times that the word we want to search appears in the grid

# method search() will seach for the word's apperance (each letter) in the grid
def search(row, col, dr, dc, index):
    global h
    if index == len(w):
        h += 1
        return
    
    # if search reaches boarder, stop
    if row < 0 or row >= r or col < 0 or col >= c or grid[row][col] != w[index]:
        return
    
    search(row + dr, col + dc, dr, dc, index + 1) # continue search for the next letter in the direction give
    
# search for the word in the grid
for i in range(r):
    for j in range(c):
        # search in all directions
        search(i, j, 1, 0, 0) # horizontal left to right
        search(i, j, -1, 0, 0) # horizontal right to left
        search(i, j, 0, 1, 0) # vertical top to bottom
        search(i, j, 0, -1, 0) # vertical bottom to top
        search(i, j, 1, 1, 0) # top-left to bottom-right
        search(i, j, -1, -1, 0) # bottom-right to top-left
        search(i, j, 1, -1, 0) # top-right to bottom-left
        search(i, j, -1, 1, 0) # bottom-left to top-right
        
print(h) # print output
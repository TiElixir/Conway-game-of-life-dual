import matplotlib
import math

grid_size=(9,9)

grid=[
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
#grid Row, Column
def getValue(x,y):
    return(grid[y][x])

def getNeighbours(x,y):
    #grid (y,x)
    return((grid[y-1][x-1])+(grid[y-1][x])+(grid[y-1][x+1])+(grid[y][x-1])+(grid[y][x+1])+(grid[y+1][x-1])+(grid[y+1][x])+(grid[y+1][x+1]))



print(getValue(1,2))

print(getNeighbours(1,2))
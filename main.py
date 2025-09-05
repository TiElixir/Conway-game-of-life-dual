import math
import time

grid_size=9
running=True
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

def getNeighbours(x, y):
    neighbours = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue  # skip self
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size:
                neighbours += grid[ny][nx]
    return neighbours
def setValue(x,y, val):
    global grid
    grid[y][x]=val

def showGrid(g):
    print(f'\n'*15)
    for x in g:
        print(x)

def emptyGrid(g):
    s=0
    for x in g:
        for y in x:
            s+=y
    return(s)
setValue(2,4,1)
setValue(3,4,1)
setValue(4,4,1)
setValue(4,3,1)
setValue(3,2,1)



print('Tick 0'+str(grid))

#Game Loop:
def tick():
    global grid
    gridTemp = [row[:] for row in grid]
    
    for y in range(grid_size):
        for x in range(grid_size):
            #Death Logic
            if(grid[y][x])==1 and getNeighbours(x,y)<=1:
                gridTemp[y][x]=0
            if(grid[y][x])==1 and getNeighbours(x,y)>=4:
                gridTemp[y][x]=0

            #Birth Logic
            if(grid[y][x])==0 and getNeighbours(x,y)==3:
                gridTemp[y][x]=1
    grid=gridTemp.copy()
    if emptyGrid(grid)==0:
        running=False
            


while running:
    showGrid(grid)
    time.sleep(1)
    tick()


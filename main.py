#.___________. __   _______  __       __  ___   ___  __  .______      
#|           ||  | |   ____||  |     |  | \  \ /  / |  | |   _  \     
#`---|  |----`|  | |  |__   |  |     |  |  \  V  /  |  | |  |_)  |    
#    |  |     |  | |   __|  |  |     |  |   >   <   |  | |      /     
#    |  |     |  | |  |____ |  `----.|  |  /  .  \  |  | |  |\  \----.
#    |__|     |__| |_______||_______||__| /__/ \__\ |__| | _| `._____|




import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random

grid_size=25
running=True
grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
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

#Test vals

for i in range(200):
    setValue(random.randint(1,24),random.randint(1,24),1)




#Game Loop:
def tick():
    global grid, running
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
            




# ---- Matplotlib Animation ----
fig, ax = plt.subplots()
img = ax.imshow(grid, cmap="binary")
ax.axis("off")

def update(frame):
    tick()
    img.set_data(grid)
    return [img]

ani = animation.FuncAnimation(fig, update, frames=200, interval=200, blit=True)

while running:
    plt.show()
    time.sleep(1)
    tick()
    
# John Burghardt
from math import *
ROWS = 33
COLS = 127
xAxis = ceil(ROWS / 2) - 1
yAxis = ceil(COLS / 2) - 1
plane = []
for i in range(ROWS) :
    plane.append([])
    for j in range(COLS) :
        plane[i].append(' ')
for i in range(1, COLS - 1) :
    plane[xAxis][i] = '-'
for i in range(1, ROWS - 1) :
    plane[i][yAxis] = '|'
plane[xAxis][COLS - 1] = '→'
plane[xAxis][0] = '←'
plane[ROWS - 1][yAxis] = '↑'
plane[0][yAxis] = '↓'
plane[xAxis][yAxis] = '+'
for x in range(-yAxis, ceil(COLS / 2)) :
    try :
        y = (1/4)*x
        if True :
            y = int(y)
        else :
            continue
    except :
        continue
    if abs(y) <= xAxis :
        plane[xAxis + y][yAxis + x] = '·'
# Graphs f(x)
while True :
    print("\033[H\033[2J", end = "")
    print("Graphing Calculator")
    for i in range(ROWS) :
        for j in range(COLS) :
            print(plane[(ROWS - 1) - i][j], end = "")
        print()
    """
      01234
      _____
    0|  ↑  
    1|  |  
    2|←-+-→
    3|  |  
    4|  ↓  
    xAxis = ceil(ROWS / 2) - 1 = ceil(5 / 2) - 1 = 3 - 1 = 2
    yAxis = ceil(ROWS / 2) - 1 = ceil(5 / 2) - 1 = 3 - 1 = 2
    xIndex = yAxis + user_x
    yIndex = xAxis + user_y
    """
    pair = input("Enter coordinates: ")
    try :
        x = int(pair[pair.find('(') + 1:pair.find(',')])
        y = int(pair[pair.find(',') + 1:pair.find(')')])
        plane[xAxis + y][yAxis + x] = '·'
    except :
        continue
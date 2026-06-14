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
while True :
    print("\033[H\033[2J", end = "")
    print("Graphing Calculator")
    for i in range(ROWS) :
        for j in range(COLS) :
            print(plane[(ROWS - 1) - i][j], end = "")
        print()
    pair = input("Enter coordinates: ")
    try :
        x = int(pair[pair.find('(') + 1:pair.find(',')])
        y = int(pair[pair.find(',') + 1:pair.find(')')])
        plane[xAxis + y][yAxis + x] = '·'
    except :
        continue
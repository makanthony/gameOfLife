# -*- coding: utf-8 -*-
"""
Wed Nov 30 2022

Anthony Mak
"""

import random as rand
import numpy as np

def fill (board):
    for x in range(20):
        for y in range(20):
            num = rand.uniform(1, 10)
            if num <= 4:
                board[x, y] = 1
    return board

'''
general rules:
1: Any live cell with two or three live neighbors survives.
2: Any dead cell with three live neighbors becomes a live cell.
3: All other live cells die in the next generation. Similarly, all other dead cells stay dead.
'''

def nghCount(board, x, y):
    ngh = 0 #counter for live neighbors
    if (board[x-1, y+1] == 1):
        ngh += 1
    if (board[x, y+1] == 1):
        ngh += 1
    if (board[x+1, y+1] == 1):
        ngh += 1
    if (board[x-1, y] == 1):
        ngh += 1
    if (board[x+1, y] == 1):
        ngh += 1
    if (board[x-1, y-1] == 1):
        ngh += 1
    if (board[x, y-1] == 1):
        ngh += 1
    if (board[x+1, y-1] == 1):
        ngh += 1
    return ngh
        
def gen(board, x, y):
    ngh = nghCount(board, x, y)
    
    if board[x, y] == 1:
        if ngh == 2 or ngh == 3:
            return board
        else:
            board[x, y] = 0
    else:
        if ngh == 3:
            board[x, y] = 1
    return board

'''
edge rules:
1: Any live cell with one or two live neighbors survives.
2: Any dead cell with two or three live neighbors becomes a live cell.
3. Any live cell without any live neighbors dies
4. Any live cell with three or more live neighbors dies
'''
def edge(board, x, y):
    ngh = 0
    if(x==0):
        if (board[x, y-1] == 1):
            ngh += 1
        if (board[x, y+1] == 1):
            ngh += 1
        if (board[x-1, y-1] == 1):
            ngh += 1
        if (board[x-1, y] == 1):
            ngh += 1
        if (board[x-1, y+1] == 1):
            ngh += 1
    elif(x==19):
        if (board[x, y-1] == 1):
            ngh += 1
        if (board[x, y+1] == 1):
            ngh += 1
        if (board[x+1, y-1] == 1):
            ngh += 1
        if (board[x+1, y] == 1):
            ngh += 1
        if (board[x+1, y+1] == 1):
            ngh += 1
    elif(y==0):
        if (board[x-1, y] == 1):
            ngh += 1
        if (board[x+1, y] == 1):
            ngh += 1
        if (board[x+1, y+1] == 1):
            ngh += 1
        if (board[x, y+1] == 1):
            ngh += 1
        if (board[x-1, y+1] == 1):
            ngh += 1   
    elif(y==19):
        if (board[x, y] == 1):
            ngh += 1
        if (board[x, y] == 1):
            ngh += 1
        if (board[x+1, y-1] == 1):
            ngh += 1
        if (board[x, y-1] == 1):
            ngh += 1
        if (board[x-1, y-1] == 1):
            ngh += 1
        
    if board[x, y] == 1:
        if ngh == 1 or ngh == 2:
            return board
        else:
            board[x, y] = 0
    else:
        if ngh == 2 or ngh == 3:
            board[x, y] = 1
    return board

'''
corner rules:
1: Any live cell with any live neighbors survives.
2: Any dead cell with any live neighbors becomes a live cell.
3. Any live cell without any live neighbors dies
'''
def corner(board, x, y):
    ngh = 0
    if x==0:
        if y==0:
            if board[x+1, y] == 1:
                ngh += 1
            if board[x+1, y-1] == 1:
                ngh += 1
            if board[x, y-1] == 1:
                ngh += 1
        else:
            if board[x, y+1] == 1:
                ngh += 1
            if board[x+1, y+1] == 1:
                ngh += 1
            if board[x+1, y] == 1:
                ngh += 1
    else:
        if y==0:
            if board[x-1, y] == 1:
                ngh += 1
            if board[x-1, y-1] == 1:
                ngh += 1
            if board[x, y-1] == 1:
                ngh += 1
        else:
            if board[x, y+1] == 1:
                ngh += 1
            if board[x-1, y+1] == 1:
                ngh += 1
            if board[x-1, y] == 1:
                ngh += 1
        if board[x, y] == 1:
            if ngh == 0:
                board[x, y] = 0
        else:
            if ngh > 0:
                board[x, y] = 1
    return board

gameBoard = np.zeros((20, 20))

fill(gameBoard)

loop = 0
x, y = 0, 0 #x-axis and y-axis
while loop == 0:
    for y in range(19):
        for x in range(19):
            if 0 < x < 19 and 0 < y < 19:
                gen(gameBoard, x, y)
            elif (x == 0 and y==0) or (x==0 and y==19) or (x==19 and y==0) or (x==19 and y==19):
                corner(gameBoard, x, y)
            else:
                edge(gameBoard, x, y)
    for row in gameBoard:
        print(row)
    print('\n')
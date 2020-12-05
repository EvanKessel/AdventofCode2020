# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:58:30 2020

@author: hidej
"""
with open("input.txt") as file:
    inp = file.read()
    
    lines = inp.split()
    
    seats = []
    
    for line in lines:
        row = 0
        col = 0
        
        for c in line[:7]:
            row <<= 1
            row += int(c == "B")
            
        for c in line[7:]:
            col <<= 1
            col += int(c == "R")
            
        seats.append((row,col))
    seats.sort(reverse = True, key = lambda s : s[0]*8 + s[1] )
    #print(seats[0][0]*8 + seats[0][1])
    seatids = list(map(lambda s : s[0]*8 + s[1], seats))
    for index in range(len(seatids)):
        if seatids[index]-1 != seatids[index+1]:
            print(seatids[index]-1)
            break
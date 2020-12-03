# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:51:02 2020

@author: hidej
"""
with open("input.txt") as file:
    inp = file.read()
    
    lines = inp.split("\n")
    
    trees = 0
    
    x = 0
    y = 0
    
    stepsx= 3
    stepsy = 1
    
    while y < len(lines)-2:
        x += stepsx
        y += stepsy
        print(x,y)
        
        if lines[y][x % len(lines[0])] == "#":
            trees += 1
            
    print(trees)
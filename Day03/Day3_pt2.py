# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:51:02 2020

@author: hidej
"""
with open("input.txt") as file:
    inp = file.read()
    
    lines = inp.split("\n")
    
    product = 1
    
    
    stepsxl = (1,3,5,7,1)
    stepsyl = (1,1,1,1,2)
    
    for stepsx,stepsy in zip(stepsxl,stepsyl):
        
        trees = 0
        
        x = 0
        y = 0
    
    
        x += stepsx
        y += stepsy
        
        while y < len(lines)-1:
            
            
            if lines[y][x % len(lines[0])] == "#":
                trees += 1
            x += stepsx
            y += stepsy
            print(x,y)   
        product *= trees    
    
    print(product)
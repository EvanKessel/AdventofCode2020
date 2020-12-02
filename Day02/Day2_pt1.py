# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 22:04:46 2020

@author: hidej
"""
with open("input.txt") as file:
    inp = file.read()
    
    lines = inp.split("\n")
    
    valid = 0
    del lines[-1]
    
    for line in lines:
        splitline = line.split()
        
        minmax = splitline[0].split("-")
        charcount = splitline[2].count(splitline[1][0])
        if int(minmax[0]) <= charcount <= int(minmax[1]):
            valid += 1
            
         
    print(valid)    
    

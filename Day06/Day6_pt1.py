# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 21:59:50 2020

@author: hidej
"""
with open("input.txt") as file:
    inp = file.read()
    
    groups = inp.split("\n\n")
    
    groups = list(map(lambda ans: set(ans.replace("\n","")), groups))
    
    count = sum(map(len,groups))
    
    print(count)
    
                  
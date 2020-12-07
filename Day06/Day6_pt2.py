# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 21:59:50 2020

@author: hidej
"""

# from functools import reduce
# with open("input.txt") as file:
#     inp = file.read()
    
#     groups = inp.split("\n\n")
    
#     groups = list(map(lambda ans: ans.split(), groups))
    
#     groups = list(map(lambda ls: reduce(lambda a,b: set(a)&set(b), ls), groups))
    
#     count = sum(map(len,groups))
    
#     print(count)

from functools import reduce; print(sum(map(len,map(lambda ls: reduce(lambda a,b: set(a)&set(b), ls),map(lambda ans: ans.split(),open("input.txt").read().split("\n\n"))))))
    
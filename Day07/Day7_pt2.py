# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:38:11 2020

@author: hidej
"""
target = "shiny gold"

def removeWords(string,words):
    output = string
    for word in words:
        output = output.replace(word,"")
    return output

def searchBags(target,rules,extbags):
    for bag in rules:
        if target in rules[bag]:
            extbags[bag] = None
            searchBags(bag, rules, extbags)

def containedBags(target,rules, isexternal = True):
    contained = 0 if isexternal else 1
    for bag in rules[target]:
        contained += rules[target][bag]*containedBags(bag, rules,False)
    return contained

with open("input.txt") as file:
    inp = file.read()
    
    lines = inp.split("\n")[:-1]
    
    rules = {}
    
    for line in lines:
        cleanline = removeWords(line,["contain","no other bags","bags","bag",".",","])
        
        splitrule = cleanline.split()
        
        outer1,outer2,*rest = splitrule
        
        rules[f"{outer1} {outer2}"] = {}
        
        for i in range(0,len(rest),3):
            rules[f"{outer1} {outer2}"][f"{rest[i+1]} {rest[i+2]}"] = int(rest[i])
         
        extbags = {}
        searchBags(target, rules, extbags)
        
    print(len(extbags))
    print(containedBags(target, rules))
       
    
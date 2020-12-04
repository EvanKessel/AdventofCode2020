# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:07:13 2020

@author: hidej
"""
with open("input.txt") as file:
    inp = file.read()
    
    passports = inp.split("\n\n")
    #print(passports)
    
    valid = 0
    params = ("byr","iyr","eyr","hgt","hcl","ecl",'pid')
    
    mapped = map(lambda string: string.split(),passports)
    #print(mapped)
    
    for passport in mapped:
       #print(passport)
        
        split = dict(map(lambda string: string.split(":"),passport))
       #print(dict(split))
       
        if all(param in split for param in params):
            valid += 1
            
    print(valid)
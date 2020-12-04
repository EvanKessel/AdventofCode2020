# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:07:13 2020

@author: hidej
"""

def checkpassport(check):
    try:
        byr = int(check["byr"])
        if not 1920 <= byr <= 2002:
            return False
        iyr = int(check["iyr"])
        if not 2010 <= iyr <= 2020:
            return False
        eyr = int(check["eyr"])
        if not 2020 <= eyr <= 2030:
            return False
        if check["hgt"][-2:] == "in":
            hgt = int(check["hgt"][0:-2])
            if not 59 <= hgt <= 76:
                return False
        elif check["hgt"][-2:] == "cm":
            hgt = int(check["hgt"][0:-2])
            if not 150 <= hgt <= 193:
                return False
        else:
            return False
        if not check["ecl"] in ("amb","blu","brn","gry","grn","hzl","oth"):
            return False
        if check["hcl"][0] == "#" and len(check['hcl']) == 7:
            if not all(char in ("0123456789abcdef") for char in check["hcl"][1:]):
                return False
        else:
            return False
        if len(check["pid"]) == 9:
            if not int(check["pid"]) > 0:
                return False
            
        else:
            return False
        
    except:
        return False
    return True


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
            if checkpassport(split):
                valid += 1
            
    print(valid)
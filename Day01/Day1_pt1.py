# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:10:54 2020

@author: hidej
"""
inp = input("Enter Input\n")
expenses = inp.split()

for index in range(len(expenses)):
    expenses[index] = int(expenses[index])
result = 0   
for num1 in expenses:
    for num2 in expenses:
        if num1 + num2 == 2020:
            result = num1 * num2
            break
        
    if result != 0:
        break

print(result)
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 15:18:36 2017

@author: jbranham
"""

s = input("Please enter a string: ")
start = 0
end = 3
numbobs = 0
for char in s:
    test = s[start:end]
    if test == "bob":
        numbobs += 1
    start += 1
    end += 1
print("Number of times bob occurs is: " + str(numbobs))
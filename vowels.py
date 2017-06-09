# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 13:26:51 2017

@author: jbranham
"""

s = input("Please enter a string of lower case numbers: ")
numvowels = 0
vowels = ('a','e','i','o','u')
for char in s:
    if char == vowels[0] or char == vowels[1] or char == vowels[2] or char == vowels[3] or char == vowels[4]:
        numvowels += 1
print("Number of vowels: " + str(numvowels))
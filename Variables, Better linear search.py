# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:16:59 2019

@author: 21359035
"""

x0 = 0
x1 = 1
x2 = 2
x3 = 3

y = 0

x0 = x1
x1 = x2
x2 = x3
x3 = y
print(x0, x1, x2, x3)

import math
radius = float(input("Enter a radius: "))
Area = math.pi * radius *radius
print(Area)

def better_linear_search(A, x):
    for i in range(0, len(A)):
        if A[i] == x: return print (i)
    return print(-1)

better_linear_search([10, 5, 9, 9], 12) 

def better_linear_search(A, x): 
    for i in range(0, len(A)):
        if A[i] == x: return print (i)
    return print(-1)

better_linear_search([10, 5, 9, 9], 50)

def better_linear_search(A, x):
    for i in range(0, len(A)):
        if A[i] == x: return print (i)
    return print (-1)

better_linear_search([10, 5, 9, 9], 8)

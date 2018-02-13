# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 22:00:29 2017

@author: Mahhita
"""

#%%

for _ in range(int(input())):
    n = int(input())
    highest = -1
    for a in range(1, int(n/3)):
        b = (n*n - 2*n*a)//(2*n - 2*a);
        c = n - a - b
        if (a * a)+(b * b) == (c * c):
            temp = a*b*c
            if temp > highest:
                highest = temp
    print(highest)

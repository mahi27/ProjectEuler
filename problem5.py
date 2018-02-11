# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 21:27:54 2017

@author: Mahhita
"""

"""
Problem 5
"""
from functools import reduce
def _gcd(x,y):
    while y!=0:
        x,y=y,x%y
    return x

t = int(input())
for _ in range(t):
    n = int(input())
    print(int(reduce(lambda x,y: x*y/_gcd(x,y), range(1,n+1))))
    
    
"""problem 6"""

def findsum(n):
    s = ((n*(n+ 1)/2.0)*(n*(n+ 1)/2.0)) - ((n*(n+1)*(2*n + 1))/6.0)
    return(int(s))

for _ in range(int(input())):
    n = int(input())
    print(findsum(n))


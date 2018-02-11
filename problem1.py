# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 20:28:31 2017

@author: Mahhita
"""

#Problem1
#%%
def art(y):
    return y*(y+1);

t = int(input())
for _ in range(t):
    n = int(input())
    n -=1;
    a=int(n/3);
    b=int(n/5);
    c=int(n/15);
    print(int(int(3*art(a) + 5*art(b) - 15*art(c))>>1));
        
#%%

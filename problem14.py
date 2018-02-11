# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 22:39:56 2017

@author: Mahhita
"""
#%%
"""Which starting number, under one million, produces the longest chain?"""

i = 1

while i < 1000000:
    if (i - 1)%3 == 0:
        k = (i-1)/3
        if k%2 == 0:
            i = i*2
        else:
            i = k
    else:
        i = i*2

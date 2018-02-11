# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 20:45:52 2017

@author: Mahhita
"""
#%%
a = []
a.append(1)
a.append(2)
#%%
i = 2
while i > 0:
    s = a[i - 1] + a[i - 2]
    if s < 4000000:
        a.append(s)
        i = i+1
    else:
        break
#%%
sum = 0
for i in a:
    if i%2 == 0:
        sum = sum + i
#%%

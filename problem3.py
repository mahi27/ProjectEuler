# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 21:07:43 2017

@author: Mahhita
"""
#%%

"""
Problem 3
"""

n = 600851475143
i = 2
while i * i < n:
     while n % i == 0:
         n = n / i
     i = i + 1
print (n)
#%%


"""
Problem 4
"""
def palindrome(r):
    return(list(str(r)) == list(reversed(str(r))))
#%%
product = 10000
for i in range(100,1000):
    for j in range(100,1000):
        pr = i*j
        if palindrome(pr) and pr > product:
            product = pr

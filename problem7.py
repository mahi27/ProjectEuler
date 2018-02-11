# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 22:11:00 2017

@author: Mahhita
"""
#%%
def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True 

primes = []
for i in range(104744):
    if is_prime(i):
        primes.append(i)

for i in range(int(input())):
    print(primes[int(input())-1])

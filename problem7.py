# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 22:11:00 2017

@author: Mahhita
"""
#%%
def is_prime(number):
      if number < 2:
            return False
      elif number == 2:
         return True
      elif number % 2 == 0:
            return False
      else:
            for i in range(3, number):
                  if not number % i:
                        return False
            return True 


#%%
#This array stores all the prime numbers found till n
primes = []
n = 10001
i = 1
while len(primes)<n:
      if is_prime(i):
            primes.append(i)
      i = i + 1
#%%
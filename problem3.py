# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 21:07:43 2017

@author: Mahhita
"""
#%%
"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""
n = 600851475143
i = 2
while i * i < n:
     while n % i == 0:
         n = n / i
     i = i + 1
print (n)
#%%
"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

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
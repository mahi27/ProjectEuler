# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 21:07:43 2017

@author: Mahhita
"""
#%%

"""
Problem 3
"""

for t in range(int(input())):
    n = int(input())
    i = 2
    high = 1
    while(i*i <= n):
        while(n%i == 0 ):
            n = n/i
            high = i
        i += 1
    if n > 1 : print(int(n))
    else: print(high)
#%%


"""
Problem 4
"""
def palindrome(r):
    return(list(str(r)) == list(reversed(str(r))))

list_palindrome = []
for i in range(100, 1000):
    for j in range(100, 1000):
        temp = i * j
        if palindrome(temp):
            list_palindrome.append(temp)
list_palindrome.sort()

for _ in range(int(input())):
    n = int(input())
    for i in range(len(list_palindrome)):
        if list_palindrome[i] >= n:
            print(list_palindrome[i-1])
            break

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 21:27:54 2017

@author: Mahhita
"""

"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10
without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
#%%
"""my solution"""
i  = 11*13*14*16*17*18*19*20
t = 11*13*14*16*17*18*19*20
check = [11,13,14,16,17,18,19,20]
k = 2
while t > 2520:
    if all(t%n == 0 for n in check):
        t = i/k 
        k = k*2
    else:
        print(t*2)
        break
#%%
"""faster"""
check_list = [11, 13, 14, 16, 17, 18, 19, 20]

def find_solution(step):
    for num in range(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None

if __name__ == '__main__':
    solution = find_solution(20)
    if solution is None:
        print("No answer found")
    else:
        print("found an answer:", solution)
#%%
"""problem 6
Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum."""

def findsum(n):
    s = ((n*(n+ 1)/2.0)*(n*(n+ 1)/2.0)) - ((n*(n+1)*(2*n + 1))/6.0)
    return(s)

findsum(100)



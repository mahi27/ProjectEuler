# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 22:13:01 2017

@author: Mahhita
"""
#%%
import numpy
def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(n/2, dtype=numpy.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1
#%%
f = primesfrom3to(2000000)
#%%
sum(f) + 2
#%%
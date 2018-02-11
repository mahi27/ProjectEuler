# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 21:40:56 2017

@author: Mahhita
"""
#%%
def produit(nbs):
    prod = 1
    for i in nbs:
        prod *= int(i)
    return prod

for _ in range(int(input())):
    n,k = input().split()
    n,k = [int(n),int(k)]
    num = input().strip()
    resultat = 0
    for i in range(n-k):
        prod = produit(num[i:i+k])
        if prod > resultat:
            resultat = prod
    print(resultat)
        

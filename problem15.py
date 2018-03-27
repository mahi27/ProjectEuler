from math import factorial
 
tc = int(input())
for _ in range(tc):
    m, n = [int(j) for j in input().split(" ")]
    print((factorial(m + n) // (factorial(m) * factorial(n))) % 1000000007)
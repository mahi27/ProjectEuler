lookup = {}
 
def countTerms(n):
    if n not in lookup:
        if n == 1:
            lookup[n] = 1
        elif not n % 2:
            lookup[n] = countTerms(n / 2)[0] + 1
        else:
            lookup[n] = countTerms(n*3 + 1)[0] + 1
 
    return lookup[n], n
 
 
for _  in range(int(input())):
    n = int(input())
    print(max(countTerms(i) for i in range(1,n+1,2))[1])
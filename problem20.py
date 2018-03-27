def factorial(n):
    if n <1:
        return 1
    else:
        returnNumber = n * factorial( n - 1 )
        return returnNumber
    
for _ in range(int(input())):
    num = factorial(int(input()))
    s = sum([int(i) for i in str(num)])
    print(s)
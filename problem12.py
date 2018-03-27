def f(L, n=42000):
	d = [0]*n
	for i in range(1, n):
		for j in range(i, n, i):
			d[j]+= 1
			c = d[i-1] * d[i//2] if i % 2 == 0 else d[(i-1)//2] * d[i]
	if c > L: return c, i*(i-1)//2
 
for _ in range(int(input())):
    L = int(input())
    Dt, t = f(L)
    print(t)
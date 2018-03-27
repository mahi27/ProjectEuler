for _ in range(int(input())):
    rows = int(input())
    w,h = rows,rows
    tri = [[0 for x in range(w)] for y in range(h)]
    for i in range(0,rows):
        x = input().split()
        tri[i][:len(x)] = list(map(int,x))
    for i in range((rows-2),-1,-1):
        for j in range(rows-1):
            tri[i][j] = tri[i][j] + max(tri[i+1][j],tri[i+1][j+1])
    print(tri[0][0])
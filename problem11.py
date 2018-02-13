grid = []
for i in range(20):
   t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
   grid.append(t)

max_prod=0
for i in range(0,20):
    for j in range(0,20):
        if(i+3<20):
            product=grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
            max_prod=max(product,max_prod)
        if(j+3<20):
            product=grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
            max_prod=max(product,max_prod)
        if(i+3<20 and j+3<20):
            product=grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
            max_prod=max(product,max_prod)
        if(i+3<20 and j-3>=0):
            product=grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3]
            max_prod=max(product,max_prod)
            
print(max_prod)

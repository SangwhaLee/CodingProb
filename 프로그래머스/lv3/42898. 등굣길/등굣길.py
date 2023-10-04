def solution(m, n, puddles):
    way = [[-1]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                way[i][j] = 1
                
    for p in puddles:
        i = p[1] - 1
        j = p[0] - 1
    
        if i == 0:
            for k in range(j,m):
                way[i][k] = 0
        elif j == 0:
            for k in range(i,n):
                way[k][j] = 0
        else:
            way[i][j] = 0
    
    for i in range(1,n):
        for j in range(1,m):
            if way[i][j] == 0:
                continue
            way[i][j] = (way[i][j-1] + way[i-1][j])
    
    return way[n-1][m-1] % 1000000007
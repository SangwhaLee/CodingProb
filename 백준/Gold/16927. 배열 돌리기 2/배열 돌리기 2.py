import sys

N,M,R = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def rotate(i,j,n,m):
    top = arr[i][j] #좌상단
    left = arr[n-1][j] #좌하단
    bottom = arr[n-1][m-1] #우하단
    right = arr[i][m-1] #우상단

    for x in range(n-1, i, -1):
        arr[x][j] = arr[x-1][j]
    for x in range(i, n-1):
        arr[x][m-1] = arr[x+1][m-1]
    for y in range(j, m-1):
        arr[i][y] = arr[i][y + 1]
    for y in range(m-1,j,-1):
        arr[n-1][y] = arr[n-1][y-1]
    
    arr[i+1][j] = top
    arr[n-1][j+1] = left
    arr[n-2][m-1] = bottom
    arr[i][m-2] = right

deep = min(N,M) //2

cycle = (N-1)*2 + (M-1)*2

for i in range(deep):
    for _ in range(R % cycle):
        rotate(i,i,N-i,M-i)
    cycle -= 8

for x in arr:
    print(*x, sep=' ')
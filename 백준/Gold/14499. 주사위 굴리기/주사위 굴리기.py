n, m, x, y, k = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

order = list(map(int,input().split()))

dice = [0,0,0,0,0,0]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def move(dir):
    a,b,c,d,e,f = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]

    if dir == 1:
        dice[3],dice[1],dice[0],dice[5],dice[4],dice[2] = a,b,c,d,e,f
    elif dir == 2:
        dice[2],dice[1],dice[5],dice[0], dice[4], dice[3] = a,b,c,d,e,f
    elif dir == 3:
        dice[4],dice[0],dice[2],dice[3],dice[5],dice[1] = a,b,c,d,e,f
    else:
        dice[1],dice[5],dice[2],dice[3],dice[0],dice[4] = a,b,c,d,e,f
    
nx,ny = x,y
for i in order:
    nx += dx[i-1]
    ny += dy[i-1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue

    move(i)
    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[-1]
    else:
        dice[-1] = arr[nx][ny]
        arr[nx][ny] = 0
    
    print(dice[0])
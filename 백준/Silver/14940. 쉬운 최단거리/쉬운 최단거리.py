from collections import deque

di = [0,-1,0,1]
dj = [-1,0,1,0]

N, M = map(int,input().split())
res = [[-1]*M for _ in range(N)]

arr= []
que = deque()

for i in range(N):
    row = list(map(int,input().split()))

    for j in range(M):
        if row[j] == 2:
            que.append((i,j))
            res[i][j] = 0
        
        if row[j] == 0:
            res[i][j] = 0
    arr.append(row)

while que:
    tmp_i, tmp_j = que.popleft()

    for k in range(4):
        ni = tmp_i + di[k]
        nj = tmp_j + dj[k]
    
        if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj] == 0 and res[ni][nj] == -1:
            que.append((ni,nj))
            res[ni][nj] = res[tmp_i][tmp_j] + 1

for row in res:
    for i in row:
        print(i, end=" ")
    print()
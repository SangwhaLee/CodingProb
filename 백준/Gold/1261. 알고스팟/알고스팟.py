from collections import deque

M, N = map(int, input().split())

arr = [list(map(int,input())) for _ in range(N)]

check = [[-1]*M for _ in range(N)]

di = [0,1,0,-1]
dj = [1,0,-1,0]

check[0][0]= 0 

def bfs():
    que = deque()
    que.append((0,0))

    while que:
        i, j = que.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if check[ni][nj] == -1:
                if arr[ni][nj] == 0:
                    check[ni][nj] = check[i][j]
                    que.appendleft((ni,nj))
                else:
                    check[ni][nj] = check[i][j] + 1
                    que.append((ni,nj))


bfs()
print(check[N-1][M-1])

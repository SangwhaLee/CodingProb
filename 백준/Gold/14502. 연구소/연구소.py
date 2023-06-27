from collections import deque
import copy


def bfs():
    que = deque()
    tmp_map = copy.deepcopy(sqr)
    for i in range(N):
        for j in range(M):
            if tmp_map[i][j] == 2:
                que.append((i,j))
    
    while que:
        tmp = que.popleft()

        for k in range(4):
            ni = tmp[0] + di[k]
            nj = tmp[1] + dj[k]

            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if tmp_map[ni][nj] == 0:
                tmp_map[ni][nj] = 2
                que.append((ni,nj))

    global answer
    cnt = 0

    for i in range(N):
        cnt += tmp_map[i].count(0)

    answer = max(answer, cnt)    


def wallbuild(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if sqr[i][j] == 0:
                sqr[i][j] = 1
                wallbuild(cnt+1)
                sqr[i][j] = 0 

di = [1,0,-1,0]
dj = [0,1,0,-1]

N, M = map(int, input().split())

sqr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
wallbuild(0)
print(answer)


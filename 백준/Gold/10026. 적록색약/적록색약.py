from collections import deque

def normal_bfs(si, sj):
    que = deque()
    que.append((si, sj))
    visited[si][sj] = 1
    while que:
        tmp = que.popleft()
        for k in range(4):
            ni = tmp[0] + di[k]
            nj = tmp[1] + dj[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if board[ni][nj] == board[tmp[0]][tmp[1]] and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                que.append((ni,nj))


def color_bfs(si, sj):
    que = deque()
    que.append((si, sj))
    visited[si][sj] = 1
    while que:
        tmp = que.popleft()
        for k in range(4):
            ni = tmp[0] + di[k]
            nj = tmp[1] + dj[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if board[tmp[0]][tmp[1]] == 'R' and (board[ni][nj] == 'R' or board[ni][nj] == 'G') and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                que.append((ni, nj))
            elif board[tmp[0]][tmp[1]] == 'G' and (board[ni][nj] == 'R' or board[ni][nj] == 'G') and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                que.append((ni, nj))
            elif board[tmp[0]][tmp[1]] == 'B' and board[ni][nj] == board[tmp[0]][tmp[1]] and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                que.append((ni, nj))


N = int(input())

board = list(list(input()) for _ in range(N))
n_cnt = 0
c_cnt = 0

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

visited = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            normal_bfs(i,j)
            n_cnt += 1

visited = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            color_bfs(i,j)
            c_cnt += 1

print(n_cnt, end=' ')
print(c_cnt)
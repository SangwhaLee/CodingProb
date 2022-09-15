from collections import deque


def bfs(si,sj):
    global visited
    que = deque()
    que.append((si, sj))
    visited[si][sj] = 1
    while que:
        i, j = que.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue
            if ni == N-1 and nj == M-1:
                cnt_list.append(visited[i][j] + 1)
            elif visited[ni][nj] == 0 and board[ni][nj] == '1':
                que.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1


N, M = map(int,input().split())

board = list(list(input()) for _ in range(N))
visited = [[0]*M for _ in range(N)]
cnt_list = []

di = [-1, 1, 0 , 0]
dj = [0, 0, -1, 1]

bfs(0, 0)

print(min(cnt_list))
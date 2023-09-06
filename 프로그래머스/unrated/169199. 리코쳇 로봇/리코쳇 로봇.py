from collections import deque

def solution(board):
    answer = 0
    n= len(board)
    m = len(board[0])
    
    di = [0,-1,0,1]
    dj = [-1,0,1,0]
    
    maps = [[-1]*m for _ in range(n)]
    
    gi = 0
    gj = 0
    
    def dfs(x,y,maps):
        que = deque()
        maps[x][y] = 0
        que.append((x,y))
        
        while que:
            i, j = que.popleft()
        
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                
                if ni < 0 or ni >= n or nj < 0 or nj >= m or board[ni][nj] == 'D':
                    continue
                
                while 0 <= ni < n and 0 <= nj < m and board[ni][nj] != 'D':
                    ni += di[k]
                    nj += dj[k]
                
                ni -= di[k]
                nj -= dj[k]
                
                if maps[ni][nj] == -1:
                    que.append((ni,nj))
                    maps[ni][nj] = maps[i][j] + 1
                    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                dfs(i,j,maps)
            
            if board[i][j] == 'G':
                gi = i
                gj = j
    
    return maps[gi][gj]
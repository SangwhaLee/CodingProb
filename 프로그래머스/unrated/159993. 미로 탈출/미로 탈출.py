from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    end_i = 0 
    end_j = 0
    lev_i = 0
    lev_j = 0
    
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    
    board = [[0]*m for _ in range(n)]
    check = [[False]*m for _ in range(n)]
    check2 = [[False]*m for _ in range(n)]
    
    
    def dfs(x,y,check, board, dest):
        que = deque()
        check[x][y] = True
        que.append((x,y))
        
        while que:
            i, j = que.popleft()
            if maps[i][j] == dest:
                return
            
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                
                if ni < 0 or ni >= n or nj < 0 or nj >= m or maps[ni][nj] == 'X':
                    continue
                    
                if not check[ni][nj]:
                    que.append((ni,nj))
                    board[ni][nj] = board[i][j] + 1
                    check[ni][nj] = True
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                dfs(i,j,check,board,'L')
            
            if maps[i][j] == 'E':
                end_i = i
                end_j = j
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'L':
                lev_i = i
                lev_j = j
                dfs(i,j,check2,board,'E')
                break
    
    if board[end_i][end_j] == 0 or board[lev_i][lev_j] == 0:
        return -1
    else:
        return board[end_i][end_j]
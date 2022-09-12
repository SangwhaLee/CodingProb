def dfs(idx, depth):
    global minimum
    if depth == N/2:
        total1 , total2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    total1 += board[i][j]
                elif not visited[i] and not visited[j]:
                    total2 += board[i][j]
        minimum = min(minimum, abs(total1-total2))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(i+1, depth+1)
            visited[i] = False


N = int(input())
board = list(list(map(int,input().split())) for _ in range(N))
visited = [False for _ in range(N)]
minimum = 1e9

dfs(0,0)
print(minimum)

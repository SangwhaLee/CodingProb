from collections import deque

tc = int(input())

def dfs(start, visited, adj, group):
    que = deque()
    visited[start] = group
    que.append(start)

    while que:
        tmp = que.popleft()

        for des in adj[tmp]:
            if not visited[des]:
                que.append(des)
                visited[des] = -1 * visited[tmp]
            elif visited[des] == visited[tmp]:
                return False
    return True

for _ in range(tc):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    
    for _ in range(E):
        f, t  = map(int, input().split())
        graph[f].append(t)
        graph[t].append(f)
    
    visited = [False]*(V+1)

    for i in range(1,V+1):
        if not visited[i]:
            result = dfs(i, visited, graph, 1)
            if not result:
                break

    print('YES' if result else 'NO')


from collections import deque

N, K = map(int, input().split())

check = [-1]*100001

def bfs(start):
    que = deque()
    que.append(start)
    check[start] = 0

    while que:
        tmp = que.popleft()

        if tmp == K:
            print(check[K])
            return
        
        for next in (tmp-1, tmp+1, tmp*2):

            if 0 <= next <= 100000 and check[next] == -1:
                if next == tmp*2:
                    check[next] = check[tmp]
                    que.appendleft(next)
                else:
                    check[next] = check[tmp] + 1
                    que.append(next)

bfs(N)

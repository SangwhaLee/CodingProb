from collections import deque

N, M = map(int, input().split())

fsh = [[] for _ in range(N)]

for _ in range(M):
    f, t = map(int, input().split())
    fsh[f].append(t)
    fsh[t].append(f)

arrive = False
check = [False]*2001


def dfs(idx, depth):
    global arrive
    check[idx] = True

    if depth == 4:
        arrive = True
        return

    for i in fsh[idx]:
        if not check[i]:
            check[i] = True
            dfs(i, depth+1)
            check[i] = False

for i in range(N):
    dfs(i,0)
    check[i] = False
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)
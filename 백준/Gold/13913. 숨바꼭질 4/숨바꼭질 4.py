from collections import deque

N, K = map(int, input().split())

check = [0]*100001
path = [0]*100001

answer = []

def move(now):
    data = []
    temp = now

    for _ in range(check[now] + 1):
        data.append(temp)
        temp = path[temp]

    print(' '.join(map(str, data[::-1])))

def bfs(start):
    global answer
    que = deque()
    que.append(start)

    while que:
        tmp = que.popleft()
        answer.append(tmp)

        if tmp == K:
            print(check[K])
            move(tmp)
            return
        
        for next in (tmp-1, tmp+1, tmp*2):
            if 0 <= next <= 100000 and check[next] == 0:
                check[next] = check[tmp] + 1
                que.append(next)
                path[next] = tmp

bfs(N)

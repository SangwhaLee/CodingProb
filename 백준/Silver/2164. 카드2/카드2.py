from collections import deque

N = int(input())

que = deque()

for i in range(N, 0, -1):
    que.append(i)
    
while len(que) > 1:
    que.pop()
    que.appendleft(que.pop())

print(que.pop())

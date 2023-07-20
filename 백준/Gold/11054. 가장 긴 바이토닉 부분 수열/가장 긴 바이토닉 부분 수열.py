N = int(input())

arr = list(map(int,input().split()))

up = [1]*N
down = [1]*N
total = [0]* N

for main in range(N):
    for u in range(main):
        if arr[u] < arr[main]:
            up[main] = max(up[main], up[u]+1)

for main in range(N-1,-1,-1):
    for d in range(N-1, main, -1):
        if arr[d] < arr[main]:
            down[main] = max(down[main], down[d]+1)

for i in range(N):
    total[i] = up[i] + down[i]

print(max(total)-1)
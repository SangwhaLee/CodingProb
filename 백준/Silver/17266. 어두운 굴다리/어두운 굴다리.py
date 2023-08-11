N = int(input())
M = int(input())
pos = list(map(int,input().split()))

diff = 0

for i in range(1, len(pos)):
    diff = max(pos[i] - pos[i-1], diff)

diff = (diff + 1) // 2

diff = max(diff, pos[0] - 0, N - pos[-1])

print(diff)
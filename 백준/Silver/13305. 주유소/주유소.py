N = int(input())

ranges = list(map(int, input().split()))

station = list(map(int,input().split()))

now = station[0]

point = [0] * N

for i in range(1, N):
    point[i] = now * ranges[i-1]
    if station[i] < now:
        now = station[i]

print(sum(point))


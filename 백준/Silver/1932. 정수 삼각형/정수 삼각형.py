N = int(input())
tri = []

for _ in range(N):
    tri.append(list(map(int,input().split())))

for i in  range(N-2, -1, -1):
    for j in range(len(tri[i])):
        tri[i][j] = max(tri[i+1][j], tri[i+1][j+1]) + tri[i][j]

print(tri[0][0])
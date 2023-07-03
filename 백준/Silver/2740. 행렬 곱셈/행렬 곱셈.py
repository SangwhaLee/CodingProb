N, M = map(int,input().split())

A = list(list(map(int,input().split())) for _ in range(N))

M, K = map(int, input().split())

B = list(list(map(int, input().split())) for _ in range(M))

result = [[0]*K for _ in range(N)]

for i in range(N):
    for k in range(K):
        a = 0
        for j in range(M):
            a += A[i][j] * B[j][k]
        result[i][k] = a

for i in range(N):
    print(*result[i])
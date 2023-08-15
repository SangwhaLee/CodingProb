N, K = map(int, input().split())

pos = list(input())

check  = [False]*N

people = 0

for i in range(N):
    if pos[i] == 'H':
        for j in range(i-K, i+K+1):
            if j < 0: j = 0
            if j >= N: continue
            if pos[j] == 'P' and not check[j]:
                people += 1
                check[j] = True
                break

print(people)
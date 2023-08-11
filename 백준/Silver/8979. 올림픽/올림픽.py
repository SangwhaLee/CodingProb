N, K = map(int, input().split())

country = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    cNum = tmp[0]
    medals = tmp[1:]
    country.append((cNum, medals))

country.sort(reverse=True, key=lambda x :(x[1][0],x[1][1],x[1][2]))

rank = [1]
before = country[0][1]
now = 1

for i in range(1,N):
    if country[i][1] == before:
        rank.append(now)
    else:
        before = country[i][1]
        now = i + 1
        rank.append(now)

for i in range(N):
    if country[i][0] == K:
        print(rank[i])
        break


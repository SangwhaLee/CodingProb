N, score, P = map(int, input().split())

if N == 0:
    print(1)
    exit()

sc_list = list(map(int, input().split()))

sc_list.append(score)

sc_list.sort(reverse=True)

rank = [1]
now = 1
before = sc_list[0]

for i in range(1,N+1):
    if sc_list[i] < before:
        now = i + 1
        before = sc_list[i]
    rank.append(now)

for i in range(N+1):
    if sc_list[i] < score:
        if i > P:
            print(-1)
            break
        else:
            print(rank[i-1])
            break
else:
    if len(sc_list) > P:
        print(-1)
    else:
        print(rank[len(sc_list) -1])
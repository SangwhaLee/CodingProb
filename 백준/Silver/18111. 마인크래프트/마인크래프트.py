import sys

N, M, stack = map(int,input().split())

ground = list(list(map(int,input().split())) for _ in range(N))

answer = sys.maxsize
floor = -1

#높이 0층에서부터 256층까지 전부 확인

for target in range(257):
    upper, lower = 0, 0

    for i in range(N):
        for j in range(M):
            tmp = target - ground[i][j]
            if tmp > 0:
                upper += tmp
            else:
                lower += abs(tmp)
        
    if lower + stack >= upper:
        if  upper + (lower*2) <= answer:
            answer =  upper + (lower*2)
            floor = target

print(answer, floor)


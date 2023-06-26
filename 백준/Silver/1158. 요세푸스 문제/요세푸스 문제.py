N, K = map(int, input().split())

numbers = [ i for i in range(1,N+1)]

answer = []
now = 0

for _ in range(N):
    now += K-1
    if now >= len(numbers):
        now = now%len(numbers)
    
    answer.append(str(numbers.pop(now)))

anstr = '<'+ ', '.join(answer)+'>'

print(anstr)
N = int(input())

schedule = []

for i in range(N):
    tmp = list(map(int, input().split()))
    schedule.append(tmp)
    
schedule.sort(key=lambda x:(x[1], x[0]))

cnt = 0
end = -1
for i in schedule:
   if i[0] >= end:
    cnt += 1
    end = i[1] 

print(cnt)
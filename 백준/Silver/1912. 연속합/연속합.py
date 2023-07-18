N = int(input())

arr = list(map(int,input().split()))

ans = -2e9
earn = 0

for num in arr:
    earn += num
    ans = max(ans, earn)
    if earn <= 0:
        earn = 0

print(ans)

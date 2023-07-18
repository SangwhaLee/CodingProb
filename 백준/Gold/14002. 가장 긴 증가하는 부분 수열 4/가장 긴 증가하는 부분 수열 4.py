N = int(input())
arr = list(map(int,input().split()))

dp = [1]*N
ans = []

for i in range(1,N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

idx = dp.index(max(dp))
st = max(dp)
for i in range(idx,-1,-1):
    if dp[i] == st:
        ans.append(str(arr[i]))
        st -= 1

ans.reverse()

print(max(dp))
print(" ".join(ans))
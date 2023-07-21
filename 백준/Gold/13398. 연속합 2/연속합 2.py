N = int(input())

arr = list(map(int, input().split()))

ans = -2e9
dp = [[0]*N for _ in range(2)]

dp[0][0] = arr[0]

if N > 1:
    for i in range(1, N):
        dp[0][i] = max(dp[0][i-1]+ arr[i], arr[i])
        dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])

        ans = max(ans, dp[0][i], dp[1][i])
    
    print(ans)
else:
    print(dp[0][0])

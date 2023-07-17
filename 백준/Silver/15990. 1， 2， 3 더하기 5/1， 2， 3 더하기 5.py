N = int(input())

dp = [[0]*4 for _ in range(100001)]
div = 1000000009
dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1
ans = []

for i in range(4, 100001):
    dp[i][3] = (dp[i-3][1]%div+dp[i-3][2]%div)%div
    dp[i][2] = (dp[i-2][1]%div+dp[i-2][3]%div)%div
    dp[i][1] = (dp[i-1][2]%div+dp[i-1][3]%div)%div

for tc in range(N):
    m = int(input())
    ans.append((dp[m][1]%div+dp[m][2]%div+dp[m][3]%div)%div)

for a in ans:
    print(a)
    
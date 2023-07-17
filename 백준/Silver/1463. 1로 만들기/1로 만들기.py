N = int(input())

dp = [0]*(N+1)


for i in range(2, N+1):
    tmp = []
    if i % 3 == 0:
        tmp.append(dp[i//3] + 1)
    if i % 2 == 0:
        tmp.append(dp[i//2] + 1)
    tmp.append(dp[i-1] + 1)
    dp[i] = min(tmp)
    
print(dp[N])
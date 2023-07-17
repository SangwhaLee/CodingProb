N = int(input())

price = list(map(int, input().split()))

dp = [0]*(N)

dp[0] = price[0]

for i in range(1,len(price)):
    tmp = []
    tmp.append(price[i])
    for j in range((i+1)//2):
        if (i+1) % (j+1) == 0:
            tmp.append(dp[j]*((i+1)//(j+1)))
        tmp.append(dp[j]+dp[(i+1)-(j+1)-1])
    dp[i] = max(tmp)

print(dp[N-1])


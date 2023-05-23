
def solution(land):
    
    dp = land
    
    for i in range(1, len(land)):
        for j in range(4):
            a, b, c = [jj for jj in range(4) if jj != j]
            dp[i][j] += max(dp[i-1][a], dp[i-1][b], dp[i-1][c])
    
    return max(dp[len(land)-1])
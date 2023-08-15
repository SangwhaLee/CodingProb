n, m = map(int, input().split())

MAX = 100*1000

dp = [[MAX]*3] + [[el]*3 for el in list(map(int, input().split()))] + [[MAX]*3]

for i in range(n-1):
    fuel = [MAX]+list(map(int, input().split()))+[MAX]

    tmp = [[MAX]*3] + [[0]*3 for _ in range(m)] + [[MAX]*3]

    for j in range(1, m+1):
        '''
        왼쪽으로 내려갈 때 사용량
        현 시점에서 오른쪽 상단 위치에서 min(수직으로 내려온 값, 오른편으로 내려온 값) + 현재 연료량
        '''
        tmp[j][0] = min(dp[j + 1][1], dp[j + 1][2]) + fuel[j]
        '''
        수직으로 내려갈 때 사용량
        현 시점에서 수직 상단 위치에서 min(오른쪽으로 내려온 값, 왼쪽으로 내려온 값) + 현재 연료량
        '''
        tmp[j][1] = min(dp[j][0], dp[j][2]) + fuel[j]
        '''
        오른쪽으로 내려갈 때 사용량
        현 시점에서 왼쪽 상단 위치에서 min(왼쪽으로 내려온 값, 수직으로 내려온 값) + 현재 연료량
        '''
        tmp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + fuel[j]

    dp = tmp

# 마지막 연료량 중 최솟값 출력
print(min(map(min, dp)))
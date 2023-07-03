def check(candy):
    global maxLen
    for i in range(N):
        xLen = 1
        yLen = 1
        for j in range(1,N):
            if candy[i][j] == candy[i][j-1]:
                xLen += 1
            else:
                xLen = 1
            maxLen = max(maxLen, xLen)

            if candy[j][i] == candy[j-1][i]:
                yLen += 1
            else:
                yLen = 1
            maxLen = max(maxLen, yLen)

di = [0,1,0,-1]
dj = [1,0,-1,0]

N = int(input())

candy = list(list(input()) for _ in range(N))

maxLen = 1

check(candy)

for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k] 
            if ni < 0 or ni >=N or nj < 0 or nj >= N:
                continue
            candy[i][j], candy[ni][nj] = candy[ni][nj], candy[i][j]
            check(candy)
            candy[i][j], candy[ni][nj] = candy[ni][nj], candy[i][j]

print(maxLen)



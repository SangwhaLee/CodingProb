E,S,M = map(int, input().split())

cnt = 1
minAns =0

# 가장 큰 값인 S의 값 28을 기준으로 28*cnt + S 를 E와 M의
# 각 값인 15, 19로 나눴을때의 나머지가 E,M과 동일하면 반복문 break
while True:
    if (cnt-E)%15==0 and (cnt-S)%28==0 and (cnt-M)%19==0:
        break
    cnt += 1

print(cnt)
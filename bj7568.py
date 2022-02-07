N = int(input())
volume = [] #처음엔 리스트 내부에 튜플을 넣는 방법이 아닌 딕셔너리로 문제를 풀고자 했지만 해결법이 쓸데없이 복잡해졌기 때문에 포기
a= []
for i in range(N):
    x,y = map(int,input().split())
    volume.append((x,y))

for i in volume: ##처음엔 c언어와 헷갈려 i의 값이 리스트 값이 아닌 인덱스로 착각 volume[i][0]과 같이 표현
    rank =1
    for j in volume:
        if j[0] > i[0]:
            if j[1] > i[1]:
                rank += 1
    a.append(rank) ##리스트로 rank의 값을 출력하려고 했으나 요구한 형태의 출력이 아니었음
    print(rank, end = " ") ## 값을 출려간 후 end를 통해 \n이 아닌 공백으로 대체가능하다는 것을 확인

    




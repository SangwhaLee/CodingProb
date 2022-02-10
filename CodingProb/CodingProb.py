M, N = map(int, input().split())

a = []
list=[]

for i in range(0,M):
    arr = input()
    a.append(arr)

for i in range(M-7):
    for j in range(N-7):
        change_by_W=0 #좌측 상단의 사각형 색이 흰색인 경우를 가정했을때 생긴는 변화수
        change_by_B=0 #좌측 상단의 사각형 색이 검은색인 경우를 가정했을때 생긴는 변화수
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 ==0:
                    if a[k][l] != 'W':
                        change_by_W += 1
                    if a[k][l] != 'B':
                        change_by_B += 1
                else: #이는 첫번째 사각형과 변이 맞닿아 있는 사각형의 경우이다.
                    if a[k][l] != 'B':  # 때문에 여기서 B가 아닌 경우 이는 change_by_W에 저장되어야 한다
                        change_by_W += 1
                    if a[k][l] != 'W':
                        change_by_B += 1

        list.append(change_by_B)
        list.append(change_by_W)


print(min(list))

#처음엔 8*8 범위를 확인하기 전에 처음 블록이 B인 경우와 W인 경우로 두가지 조건을 나누어 각각
#반복하고 두 값의 결과를 확인해 더 작은경우를 리스트에 저장하는 방법으로 진행하려 했으나
#코드의 가시성이 안좋아지고 코드가 쓸데없이 복잡해져서 두가지 경우를 한번에 확인하는 방법으로
#변경                             
                   

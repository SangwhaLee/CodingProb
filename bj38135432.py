A, B, C= map(int, input().split())
D = int(input())

if D >= 3600:
    hour = D//3600
    min = (D%3600)//60
    sec = (D%3600)%60
elif D >= 60:
    hour= 0
    min = D//60
    sec = D%60
else:
    hour=0
    min=0
    sec = D

hour+= A
min += B
sec += C

if sec>=60:
    min += sec//60
    sec -= (sec//60)*60

if min>=60:
    hour += min//60
    min -= (min//60)*60

if hour >= 24:
    hour -= (hour//24)*24

print(hour, min, sec)

## 처음에 난 오류는 파이썬의 연산자 실수로 //를 사용해야 하는것을 /만을 사용해서 오류 발생
## 그 다음 오류는 입력받는 초의 값이 충분히 큰 경우를 생각하지 못하고 시간과 분의 증가량을 1로 고정해서 오류 발생
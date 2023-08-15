N, X = map(int,input().split())

visits = list(map(int,input().split()))

max_visitors = 0

days = 1

left =  0
right = 0
visitors = visits[0]

while right < N:
    if right - left + 1 == X:
        if visitors == max_visitors:
            days += 1
        elif visitors > max_visitors:
            max_visitors = visitors
            days = 1
        visitors -= visits[left]
        left += 1
    elif right - left + 1 < X:
        right += 1
        if right == N:
            break
        visitors += visits[right]

if max_visitors == 0:
    print("SAD")
else:
    print(max_visitors)
    print(days)

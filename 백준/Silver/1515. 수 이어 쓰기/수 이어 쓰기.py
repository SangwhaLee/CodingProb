S = input()
idx = 0 

while True:
    idx += 1
    num = str(idx)

    while len(num) > 0 and len(S) > 0:
        if num[0] == S[0]:
            S = S[1:]
        num = num[1:]

    if S == '':
        print(idx)
        break

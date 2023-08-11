N = int(input())

first = False

tray = list(list(input()) for _ in range(N))

heart = [0,0]
la = [0,0]
ra = [0,0]
waste = [0,0]
ll = [0,0]
rl = [0,0]

la_len =  0
ra_len = 0
waste_len = 0
ll_len = 0
rl_len = 0

for i in range(N):
    for j in range(N):
        if tray[i][j] == '*' and not first:
            first = True
            heart[0] = i + 1
            heart[1] = j
            break
    
    if first:
        break

la[0] = heart[0]
la[1] = heart[1] - 1
ra[0] = heart[0]
ra[1] = heart[1] + 1
waste[0] = heart[0] + 1
waste[1] = heart[1]

for k in range(la[1], -1, -1):
    if tray[la[0]][k] == '*':
        la_len += 1
    else:
        break

for k in range(ra[1], N):
    if tray[ra[0]][k] == '*':
        ra_len += 1
    else:
        break

for k in range(waste[0], N):
    if tray[k][waste[1]] == '*':
        waste_len += 1
    else:
        ll[0] = k
        ll[1] = waste[1] - 1
        rl[0] = k
        rl[1] = waste[1] + 1
        break

for k in range(ll[0], N):
    if tray[k][ll[1]] == '*':
        ll_len += 1
    else:
        break

for k in range(rl[0], N):
    if tray[k][rl[1]] == '*':
        rl_len += 1
    else:
        break

print(heart[0]+1, heart[1]+1)
print(la_len, ra_len, waste_len, ll_len, rl_len)
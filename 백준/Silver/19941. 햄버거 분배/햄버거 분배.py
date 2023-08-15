N, K = map(int, input().split())

pos = list(input())

hdx = []
pdx = []
people= 0 

for i in range(N):
    if pos[i] == 'H':
        hdx.append(i)
    else:
        pdx.append(i)

for h in hdx:
    for j in range(h-K,h+K+1):
        if j in pdx:
            idx = pdx.index(j)
            pdx.pop(idx)
            people += 1
            break
    
print(people)
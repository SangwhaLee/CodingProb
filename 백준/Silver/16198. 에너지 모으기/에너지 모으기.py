N = int(input())

energy = list(map(int,input().split()))

en = []

def dfs(step, sums, energy):
    if step == N - 2:
        en.append(sums)
        return
    
    for i in range(1,len(energy)-1):
        tmp = energy[i-1] * energy[i+1]
        dfs(step + 1, sums + tmp, energy[:i]+energy[i+1:])

dfs(0, 0, energy)

print(max(en))
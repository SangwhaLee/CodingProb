import copy
from collections import deque

def dfs(elecs, start, n):
    que = deque()
    check = [False] * (n+1)
    check[start] = True
    que.append(start)
    stack = 0
    while que:
        tmp = que.pop()
        stack += 1
        for e in elecs[tmp]:
            if not check[e]:
                que.append(e)
                check[e] = True
    
    return stack
    
def solution(n, wires):
    answer = -1
    elecs = dict()
    ans = n
    for wr in wires:
        if wr[0] not in elecs:
            elecs[wr[0]] = [wr[1]]
        else:
            elecs[wr[0]].append(wr[1])
        if wr[1] not in elecs:
            elecs[wr[1]] = [wr[0]]
        else:
            elecs[wr[1]].append(wr[0])
    
    
    for wr in wires:
        tmp = copy.deepcopy(elecs)
        one = wr[0]
        two = wr[1]
        tmp[one].remove(two)
        tmp[two].remove(one)
        r1 = dfs(tmp, one, n)
        r2 = dfs(tmp, two, n)
        ans = min(ans, abs(r1-r2))
        
    return ans
from collections import deque

def solution(numbers):
    que = deque()
    answer = [0] * len(numbers)
    maxVal = max(numbers)
    
    for idx, num in enumerate(numbers):
        if que:
            while que and que[-1][1] < num:
                tmp = que.pop()
                answer[tmp[0]] = num
            que.append((idx, num))
        else:
            que.append((idx,num))
            
    while que:
        tmp = que.pop()
        answer[tmp[0]] = -1
        
    return answer
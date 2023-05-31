from collections import deque

def solution(number, k):
    length = len(number) - k
    
    que = deque()
    
    for idx,num in enumerate(number):
        
        if not que:
            que.append(num)
        else:
            if que[-1] < num:
                while que and que[-1] < num and (len(que) + len(number) - idx > length):
                    que.pop()
                que.append(num)
            else:
                que.append(num)
        
    if len(que) > len(number) - k:
        while len(que) > len(number) - k:
            que.pop()
    answer = ''.join(que)
    return answer
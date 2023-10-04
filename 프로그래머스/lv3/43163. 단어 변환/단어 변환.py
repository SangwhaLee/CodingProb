from collections import deque

def solution(begin, target, words):
    answer = 0
    wlen = len(words[0])
    
    if target not in words:
        return 0
    
    que = deque()
    que.append((0,begin))
    check = [False]*len(words)
    
    while que:
        now_num, now_word = que.popleft()
        if now_word == target:
            return now_num
        
        for i in range(len(words)):
            tmp = 0 
            for j in range(wlen):
                if now_word[j] != words[i][j]:
                    tmp += 1
            
            if tmp == 1 and not check[i]:
                que.append((now_num+1, words[i]))
                check[i] = True
    
    return 0
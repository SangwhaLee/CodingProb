def solution(picks, minerals):
    answer = 0
    
    minerals = minerals[:sum(picks)*5]
    status = []
    total = []
    
    tmp = []
    
    for m in minerals:
        if m == 'diamond':
            status.append(25)
        elif m == 'iron':
            status.append(5)
        else:
            status.append(1)
    
    for i in range(len(minerals)):
        if i % 5 == 4 or i == len(minerals)-1:
            tmp.append(status[i])
            total.append(tmp)
            tmp = []
        else:
            tmp.append(status[i])
    
    total.sort(reverse= True, key=lambda x:sum(x))
    
    for li in total:
        if picks[0] > 0:
            for l in li:
                answer += 1
            picks[0] -= 1
        elif picks[1] > 0:
            for l in li:
                if l >= 5:
                    answer += l//5
                else:
                    answer += 1
            picks[1] -= 1
        elif picks[2] > 0:
            for l in li:
                answer += l
            picks[2] -= 1
        
        
    return answer
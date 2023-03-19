def solution(dots):
    answer = 0
    set1 = []
    set2 = []
    
    for i in range(3):
        set1.append(dots[i])
        for j in range(i+1, 4):
            set1.append(dots[j])
            for k in range(4):
                if dots[k] not in set1:
                    set2.append(dots[k])
            if abs(set1[0][1] - set1[1][1]) / abs(set1[0][0] - set1[1][0]) == abs(set2[0][1] - set2[1][1]) / abs(set2[0][0] - set2[1][0]):
                answer = 1
                break
            
    
    return answer
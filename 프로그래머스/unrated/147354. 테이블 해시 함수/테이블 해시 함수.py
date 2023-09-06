def solution(data, col, row_begin, row_end):
    answer = 0
    c = col - 1
    data.sort(key=lambda x: (x[c], -x[0]))
    S = []
    
    for i in range(row_begin-1, row_end):
        tmp = 0
        for r in data[i]:
            tmp += r % (i+1)
        S.append(tmp)
    
    result = S[0]
    
    for i in range(1, len(S)):
        result ^= S[i]
        
    return result
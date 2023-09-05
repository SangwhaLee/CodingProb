def solution(sequence, k):
    left = 0 
    right = 0
    stack = sequence[0]
    ans = []
    
    if stack == k:
        return [0,0]
    
    while right < len(sequence):
        if stack < k:
            right += 1
            if right < len(sequence):
                stack += sequence[right]
        else: 
            left += 1
            stack -= sequence[left - 1]
        if stack == k:
            ans.append([left, right])
    
    ans.sort(key= lambda x:(x[1]-x[0], x[0]))
    
    return ans[0]




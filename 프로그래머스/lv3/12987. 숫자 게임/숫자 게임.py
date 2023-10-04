def solution(A, B):
    answer = 0
    B.sort()
    
    for a in A:
        start = 0
        end = len(B) - 1
        while start < end:
            mid = (start + end) // 2
            
            if B[mid] > a:
                end = mid
            else:
                start = mid + 1
        if B[start] > a:
            answer += 1
            B.pop(start)
    
    return answer
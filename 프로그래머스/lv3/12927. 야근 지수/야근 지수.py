import heapq

def solution(n, works):
    answer = 0
    max_hq = []
    heapq.heapify(max_hq)
    
    for w in works:
        heapq.heappush(max_hq, (-w, w))
    
    for i in range(n):
        if not max_hq:
            break
        tmp = heapq.heappop(max_hq)[1]
        if tmp != 0:
            heapq.heappush(max_hq, (-(tmp-1), (tmp-1)))

    while max_hq:
        tmp = heapq.heappop(max_hq)[1]
        answer += tmp**2
    
    return answer
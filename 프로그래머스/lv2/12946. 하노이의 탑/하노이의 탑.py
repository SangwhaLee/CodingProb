def solution(n):
    answer = []
    def move(start, dest):
        answer.append([start, dest])
        
    def hanoi(N,start,dest,via):
        if N == 1:
            move(start,dest)
        else:
            hanoi(N-1, start,via,dest)
            move(start, dest)
            hanoi(N-1, via, dest, start)
    
    hanoi(n,1,3,2)
    return answer
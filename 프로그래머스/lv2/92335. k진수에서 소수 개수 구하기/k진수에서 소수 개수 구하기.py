import math

def solution(n, k):
    answer = 0
    chNum = ''
    tmp = n
    while n >= k:
        chNum = str(n%k) + chNum
        n = n//k
    
    chNum = str(n) + chNum
    
    nums = chNum.split('0')
    
    
    for nb in nums:
        if nb != '' and nb!='1':
            num = int(nb)
            for i in range(2,math.floor(math.sqrt(num))+1):
                if num%i == 0:
                    break
            else:
                answer += 1
            
    return answer
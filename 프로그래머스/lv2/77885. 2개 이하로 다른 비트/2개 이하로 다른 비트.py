def solution(numbers):
    answer = []
    
    for num in numbers:
        binNum = '0b'+'0'+bin(num)[2:]
        idx = binNum.rfind('0')
        if idx == len(binNum) - 1:
            binNum = binNum[:idx] + '1'
        else:
            binNum = binNum[:idx] + '10' + binNum[idx+2:]

        answer.append(int(binNum,2))
            
    return answer
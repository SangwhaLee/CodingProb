def solution(sequence):
    answer = 0
    seq1 = []
    seq2 = []
    
    one = 1
    two = -1
    for s in sequence:
        seq1.append(s*one)
        seq2.append(s*two)
        one *= -1
        two *= -1
    
    for i in range(1, len(sequence)):
        seq1[i] = max(seq1[i-1]+seq1[i], seq1[i], 0)
        seq2[i] = max(seq2[i-1]+seq2[i], seq2[i], 0)
    
    answer = max(max(seq1), max(seq2))    
    
    return answer
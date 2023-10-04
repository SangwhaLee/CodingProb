def solution(genres, plays):
    answer = []
    n = len(genres)
    gr_num = dict()
    gr_play = dict()
    
    for i in range(n):
        if genres[i] not in gr_num:
            gr_num[genres[i]] = []
        gr_num[genres[i]].append(i)
        if genres[i] not in gr_play:
            gr_play[genres[i]] = 0
        gr_play[genres[i]] += plays[i]
    
    high_g = sorted(gr_play, key = lambda x: gr_play[x], reverse=True)
    
    for g in high_g:
        high_p = sorted(gr_num[g], key = lambda x: (plays[x],-x), reverse = True)
        answer += high_p[0:2]
            
    return answer
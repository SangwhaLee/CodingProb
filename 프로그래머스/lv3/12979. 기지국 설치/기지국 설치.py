def solution(n, stations, w):
    answer = 0
    rg = 2*w + 1
    st = []
    
    for s in stations:
        st.append([s-w,s+w])
    
    now = 0
    for s in st:
        if s[0] <= now:
            now = s[1]
            continue
        blank = s[0] - now - 1
        answer += blank // rg
        if blank % rg:
            answer += 1
        now = s[1]
    if now < n:
        blank = n - now
        answer += blank // rg
        if blank % rg:
            answer += 1
    
    return answer
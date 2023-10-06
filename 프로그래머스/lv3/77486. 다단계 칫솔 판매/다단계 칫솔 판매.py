def solution(enroll, referral, seller, amount):
    def dfs(seller, money):
        if pair[seller] == "-":
            your = (money // 10)
            mine = money -  your
            total[seller] += mine
        else:
            your = (money // 10)
            mine = money -  your
            total[seller] += mine
            if your != 0:
                dfs(pair[seller], your)

    
    total = {enroll[i]:0 for i in range(len(enroll))}
    pair = {enroll[i]:referral[i] for i in range(len(enroll))}
    
    for i in range(len(seller)):
        dfs(seller[i], 100*amount[i])
    
    answer = list(total.values())
    
    return answer
def solution(skill, skill_trees):
    answer = 0
    skills = list(skill)
    tree = dict()
    
    for i in range(len(skill)-1,-1,-1):
        if i ==0:
            tree[skills[i]] = 0
        else:
            tree[skills[i]] = skills[i-1]
    
    print(tree)
    
    for tr in skill_trees:
        last = ''
        for sk in tr:
            if sk in skills:
                if tree[sk] == 0:
                    last = sk   
                else:
                    if last == tree[sk]:
                        last = sk
                    else:
                        break
                        
        else:
            answer += 1
    return answer
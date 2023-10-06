from collections import deque

def solution(tickets):
    def travel(start, route, check, ans):
        if len(ans) == len(tickets) + 1:
            answer.append(ans.copy())
            return
        
        try:
            for i in range(len(route[start])):
                if not check[start][i]:
                    check[start][i] = True
                    ans.append(route[start][i])
                    travel(route[start][i], route, check, ans)
                    ans.pop()
                    check[start][i] = False
        except:
            return
        
    answer = []
    route = dict()
    
    for t in tickets:
        if t[0] not in route:
            route[t[0]] = [t[1]]
        else:
            route[t[0]].append(t[1])
        
    sorted_route = {key: sorted(value) for key, value in route.items()}
    route_check = {key: [False] * len(value) for key, value in sorted_route.items()}
    
    travel("ICN", sorted_route, route_check, ["ICN"])
    
    return answer[0]
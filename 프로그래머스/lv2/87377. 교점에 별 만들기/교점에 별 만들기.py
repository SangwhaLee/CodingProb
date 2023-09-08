def solution(line):
    answer = []
    points = []
    
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            a1,b1,c1 = line[i][0], line[i][1], line[i][2]
            a2,b2,c2 = line[j][0], line[j][1], line[j][2]
            
            if (a1*b2 - a2*b1) == 0:
                continue
            
            p1 = ((b1*c2 - b2*c1) / (a1*b2  - a2*b1))
            p2 = ((c1*a2 - a1*c2) / (a1*b2 - b1*a2))
            if p1.is_integer() and p2.is_integer():
                points.append([int(p1), int(p2)])
    
    min_x = float('inf')
    max_x = -float('inf')
    min_y = float('inf')
    max_y = -float('inf')
    
    for point in points:
        min_x = min(min_x, point[0])
        min_y = min(min_y, point[1])
        max_x = max(max_x, point[0])
        max_y = max(max_y, point[1])
    
    star = [["."]*(max_x - min_x + 1) for _ in range(max_y - min_y + 1)]    
    
    for point in points:
        tmp_x = point[0] - min_x
        tmp_y = -(point[1] - max_y)
        
        star[tmp_y][tmp_x] = '*'
        
    for s in star:
        answer.append("".join(s))
    
    return answer
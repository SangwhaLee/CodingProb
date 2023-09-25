def solution(triangle):
    answer = 0
    h = len(triangle)
    
    for i in range(h-2, -1, -1):
        for j in range(len(triangle[i])):
            now = triangle[i][j]
            triangle[i][j] = max(triangle[i+1][j] + now, triangle[i+1][j+1] + now)
    
    return triangle[0][0]
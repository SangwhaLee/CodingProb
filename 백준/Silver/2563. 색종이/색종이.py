num = int(input())
square = [[0]*100 for _ in range(100)]
sqr = []

for _ in range(num):
    j, i = map(int, input().split())
    
    for k in range(10):
        for l in range(10):
            square[i+k][j+l] += 1

intersection = 0

for i in range(100):
    for j in range(100):
        if square[i][j] > 0:
            intersection += 1

print(intersection)
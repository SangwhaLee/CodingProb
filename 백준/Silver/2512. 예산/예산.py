N = int(input())

budgets = list(map(int,input().split()))

M = int(input())

if sum(budgets) <= M:
    print(max(budgets))
    exit()

budgets.sort()

start, end = 0, max(budgets)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in budgets:
        if i > mid:
            total += mid
        else:
            total += i
    
    if total <= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
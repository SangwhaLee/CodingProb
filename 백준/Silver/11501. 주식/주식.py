for _ in range(int(input())):
    N = int(input())
    stock = list(map(int,input().split()))
    total = [0]*N

    top = stock[-1]
    for i in range(N-2, -1, -1):
        if stock[i] <= top:
            total[i] = top - stock[i]
        else:
            top = stock[i]
    
    print(sum(total))
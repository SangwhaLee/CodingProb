T = int(input())

for tc in range(T):
    N, target = map(int, input().split())
    prints = list(map(int, input().split()))
    print_idx = [ i for i in range(N)]
    stack = 0

    while len(prints) > 0:
        if prints[0] < max(prints):
            prints.append(prints.pop(0))
            print_idx.append(print_idx.pop(0))
        else:
            stack += 1
            prints.pop(0)
            tmp = print_idx.pop(0)
        
            if tmp == target:
                print(stack)
                break
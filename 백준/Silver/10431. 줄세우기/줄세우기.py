for tc in range(1,int(input()) + 1):
    tmp = list(map(int,input().split()))
    steps = 0 
    line = [tmp[1]]


    for i in range(2, len(tmp)):
        for j in range(len(line)):
            if tmp[i] < line[j]:
                steps += (len(line) - j)
                line = line[:j] + [tmp[i]] + line[j:]
                break
        else:
            line.append(tmp[i])

    print(tc, end=" ")
    print(steps)


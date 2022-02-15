wanted = int(input())

rank = 0
i = 666

while 1:
    change = str(i)
    if change.find("666") != -1:
        rank +=1
        if rank == wanted:
            answer = i
            break
    i += 1

print(answer)
string = input()

idx_lst = []
tag_lst = []
chidx_lst = []
chunk_lst = []
total_lst = []
answer = ''

if '<' in string:
    for i in range(len(string)):
        if string[i] == '<':
            j = i + 1
            while string[j] != '>':
                j += 1

            idx_lst.append([i,j,True])

    chidx_lst.append([0,idx_lst[0][0]-1,False])
    for i in range(1,len(idx_lst)):
        tmp = [idx_lst[i-1][1]+1,idx_lst[i][0]-1,False]
        chidx_lst.append(tmp)
    chidx_lst.append([idx_lst[len(idx_lst)-1][1]+1,len(string)-1,False])

    total_lst = idx_lst + chidx_lst

    total_lst.sort(key=lambda x: (x[0],x[1]))

    for idx in total_lst:
        if idx[2]:
            answer = answer + string[idx[0]:idx[1]+1]
        else:
            if idx[0] <= idx[1]:
                tmp = string[idx[0]:idx[1]+1].split(" ")
                tmp_lst = []
                for ch in tmp:
                    tmp_lst.append("".join(reversed(ch)))
                answer = answer + " ".join(tmp_lst)

else:
    chunk_lst = string.split(' ')
    answer_lst = []
    for ch in chunk_lst:
        answer_lst.append("".join(reversed(ch)))
    answer = " ".join(answer_lst)

print(answer)
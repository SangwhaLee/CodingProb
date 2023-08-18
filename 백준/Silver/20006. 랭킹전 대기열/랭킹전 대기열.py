p, m = map(int, input().split())

room = []

for _ in range(p):
    level, name = map(str, input().split())
    level = int(level)

    for r in room:
        if r[0][0] <= level <= r[0][1] and len(r)-1 < m:
            r.append((level,name))
            break
    else:
        room.append([(level-10,level+10),(level,name)])

for r in room:
    if len(r) > m:
        print("Started!")
    else:
        print("Waiting!")
    tmp = r[1:]
    tmp.sort(key=lambda x:x[1])
    for pl in tmp:
        print(pl[0], pl[1])

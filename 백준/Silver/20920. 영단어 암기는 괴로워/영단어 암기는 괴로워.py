N, M = map(int, input().split())

dictionary = dict()

words = set()

for _ in range(N):
    tmp = input()
    if len(tmp) >= M:
        words.add(tmp)
        if tmp not in dictionary:
            dictionary[tmp] = 1
        else:
            dictionary[tmp] += 1

words = list(words)
words.sort(key=lambda x:(-dictionary[x], -len(x), x))

for w in words:
    print(w)
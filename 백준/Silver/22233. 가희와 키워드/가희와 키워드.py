import sys
input=sys.stdin.readline
n,m = map(int,input().split())
keywords = {input().rstrip() for _ in range(n)}
for _ in range(m):
    for key in input().rstrip().split(','):
        keywords.discard(key)
    print(len(keywords))
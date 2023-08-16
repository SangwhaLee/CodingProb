S = input()

zero = 0
one = 0

for s in S:
    if s == '0':
        zero += 1
    else:
        one += 1

answer = ""

for _ in range(zero//2):
    answer = answer + '0'
for _ in range(one//2):
    answer = answer + '1'

print(answer)
length = int(input())
numbers = []

for i in range(length):
    num = int(input())
    if num == 0:
        numbers.pop()
    else:
        numbers.append(num)

print(sum(numbers))
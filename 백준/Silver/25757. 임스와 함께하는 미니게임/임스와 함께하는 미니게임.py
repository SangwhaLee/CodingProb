game = { 'Y': 1, 'F': 2, 'O': 3}

N, g = input().split()

members = set()

for _ in range(int(N)):
    members.add(input())

print(len(members)//game[g])
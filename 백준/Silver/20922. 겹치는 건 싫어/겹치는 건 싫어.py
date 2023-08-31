N, K = map(int, input().split())

nums = list(map(int,input().split()))

L = 0
R = 0
maxLen = 1

check_to = set(nums)
check = dict()

for n in check_to:
    check[n] = 0

check[nums[R]] += 1

while R < N - 1:
    if check[nums[R]] <= K:
        R += 1
        check[nums[R]] += 1
        if check[nums[R]] <= K:
            maxLen = max(maxLen, R - L + 1)
    else:
        check[nums[L]] -= 1
        L += 1

print(maxLen)


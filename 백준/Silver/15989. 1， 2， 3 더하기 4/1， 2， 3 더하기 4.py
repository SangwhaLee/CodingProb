nums = [1]* 10001

for i in range(2, 10001):
    nums[i] += nums[i-2]

for i in range(3,10001):
    nums[i] += nums[i-3]

for tc in range(int(input())):
    n = int(input())
    print(nums[n])


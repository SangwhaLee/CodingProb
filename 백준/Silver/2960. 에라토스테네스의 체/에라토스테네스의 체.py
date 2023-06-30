# 2부터 N 까지의 리스트 생성
N, K = map(int,input().split())

nums = list(i for i in range(2,N+1))
answer = []

step = 0

while nums:
    tmp = nums.pop(0)
    answer.append(tmp) 

    for i in range(2,N//tmp+1):
        if tmp*i in nums:
            answer.append(nums.pop(nums.index(tmp*i)))

print(answer[K-1])
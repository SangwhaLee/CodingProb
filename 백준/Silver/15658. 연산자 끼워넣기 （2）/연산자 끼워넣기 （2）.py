N = int(input())

nums = list(map(int, input().split()))

operand = list(map(int,input().split()))

rs = []

def dfs(step, result, operand):
    global rs
    if step == N:
        rs.append(result)
        return
    
    for i in range(4):
        if i == 0:
            if operand[i] > 0:
                operand[i] -= 1
                dfs(step+1, result + nums[step], operand)
                operand[i] += 1
        elif i == 1:
            if operand[i] > 0:
                operand[i] -= 1
                dfs(step+1, result - nums[step], operand)
                operand[i] += 1
        elif i == 2:
            if operand[i] > 0:
                operand[i] -= 1
                dfs(step+1, result * nums[step], operand)
                operand[i] += 1
        else:
            if operand[i] > 0:
                operand[i] -= 1
                dfs(step+1, int(result / nums[step]), operand)
                operand[i] += 1

dfs(1, nums[0], operand)
print(max(rs))
print(min(rs))
num = int(input())
arr = []
for i in range(num):
  temp = int(input())
  arr.append(temp)

length = len(arr)

#배열을 정렬하기 위해서는 기준이 되는 값이 필요하다
for i in range(length-1):#기준이 되는 값이 배열 전체를 순환하도록 범위 지정
  for j in range(i+1,length):#교체되는 값은 기준이 되는 값이외의 값이 되도록 범위 지정
    if arr[j]<arr[i]:
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp

for i in arr:
  print(i)
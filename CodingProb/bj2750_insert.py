#버블정렬외 N(O^2)를 가지는 정렬인 삽입 정렬의 코드
num = int(input())
arr = []
for i in range(num):
  temp = int(input())
  arr.append(temp)

length = len(arr)

#배열의 두번째 값부터 기준이 되는 값이 시작한다
for i in range(1,length):
  key = arr[i]
  position = i
  #기준이 되는 값보다 앞에 졵재하는 값들을 key값과 차례대로 비교한다 이때 만약 비교되는 값이 key값보다 클경우 둘의 위치를 교환한다 이 교환은 key값보다 작은 값이 나오거나 위치값이 0과 같아지는 경우 끝난다.
  while position>0 and arr[position-1] > key:
    arr[position] = arr[position-1]
    position -= 1
  arr[position] = key

  

for i in arr:
  print(i)
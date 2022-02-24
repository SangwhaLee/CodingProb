#먼저 최소 힙정렬을 구현해야한다 완전2진트리를 가정하여 좌측의 자식 노드는 부모노드의 인덱스보다 2배가 크며 우측 노드는 2배+1의 값이 되도록한다.
#
def heapify(arr, index, heap_size):
 smallest = index
 left_index = 2*index
 right_index = 2*index+1
 #현재 인덱스의 자식노드의 키값이 위치하고 있는 인덱스 값이 전체 힙사이즈보다 크지 않고 현재 리스트 내 해당 인덱스 값의 키가 부모노드의 키값보다 작을 경우 둘의 값의 위치를 바꿔야 한다.
 if left_index<heap_size and arr[smallest] > arr[left_index]:
   smallest = left_index
 if right_index < heap_size and arr[smallest] > arr[right_index]:
   smallest = right_index
 if smallest != index:
   arr[smallest], arr[index] = arr[index], arr[smallest]
   heapify(arr, smallest, heap_size)

#
def heap_sort(arr):
  length = len(arr)
  arr = [0]+arr #0번 인덱스의 키값은 비워놓는다

#마지막 키값부터 1번 키값까지 순차적으로 진행하여 힙을 구성한다.
  for i in range(length, 0, -1):
    heapify(arr, i, length)

  for i in range(length, 0, -1):
    #1번 인덱스의 키값을 출력한 뒤 힙사이즈를 점차적으로 줄이며 힙을 재구성한다. 힙사이즈가 0이 될때까지 반복
    print(arr[1]) 
    arr[i], arr[1] = arr[1], arr[i]
    heapify(arr, 1, i-1)

num = int(input())
arr = []
for i in range(num):
  temp = int(input())
  arr.append(temp)

heap_sort(arr)
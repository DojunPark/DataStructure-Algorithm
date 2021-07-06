# 배열(array) -> 파이썬의 리스트(list)

'''
1. 리스트 a에 4개의 값을 할당함
2. a의 2번째 값에 1을 더하여 갱신함
리스트 a의 원소는 연속된 메모리 주소상에 저장되는 것이 아니라, 각기 다른 메모리 주소 값을 가지고 있음
'''

# 리스트 생성
a = [2, 4, 0, 5]

# a[2]를 갱신할 때 가리키고 있는 주소의 값이 변하는 것이 아니고,
# 다른 메모리 주소에 새로 만들어진 값이 생성되고 포인터가 그곳을 가리키게 되는 것
a[2] += 1
print(a[2])

# 리스트 [삽입] 연산
# 맨 뒤에 6을 삽입 -> 임의의 곳에 6이 생성되고 a[6]이 그곳을 가리킴
a.append(6)
print(a)

# 1번째 위치에 5를 삽입
a.insert(1, 5)
print(a)

# 리스트 [삭제] 연산
# 맨 뒤의 값을 지우고 리턴 -> 리턴 후 마지막 포인터를 없앰
print(a.pop())
print(a)

# i번째 값을 지우고 리턴 -> 리턴 후 i번째 포인터를 없앰
print(a.pop(1))
print(a)

# a에서 해당하는 첫번째 값을 삭제하고 앞으로 땡김
a.remove(4)
print(a)

# 리스트 [탐색] 연산
print(a.index(2))  # 해당 value의 인덱스를 반환
print(a.count(2))  # 리스트 내에서 해당 value의 갯수를 반환


'''
* c와 python의 array(list) 차이점?
- c에서는 읽기와 쓰기 연산 밖에 제공되지 않음
- python에서는 읽기 쓰기 외에도, 삽입, 삭제, 탐색 연산이 가능함
- 또한 파이썬 list는 자신의 용량을 자동으로 조절함 -> "dynamic array"
'''
import sys
a = []  # empty list
print(sys.getsizeof(a))  # a가 차지하는 메모리 bite는 56 (정수 14개 들어가는 자리)

a.append(1)
print(sys.getsizeof(a))  # 88로 늘어남 (정수 22개 들어갈 수 있는 자리) -> 파이썬이 스스로 유동적으로 자리를 증가하였음


'''
* a.append()의 작동 원리?
a에 저장될 값의 갯수 < a의 capacity인 경우
-> a[n] = value
a에 저장될 값의 갯수 > a의 capacity인 경우
-> b = a.capacity *2  # 임시로 리스트 b를 만들고,
   for i in range(n):
       b[1] = a[2]    # a의 값을 큰 집 b로 옮김
   del a    # a 삭제
   
'''


a = [1, 2, 3]
print(sys.getsizeof(a))

a.pop()
print(sys.getsizeof(a))


'''
[순차적 자료구조 소개]

리스트(배열) 외의 순차적 자료구조 -> 제한된 접근(삽입, 삭제)만 허용
- stack: LIFO (Last In First Out) - 마지막으로 입력한 순으로 삭제(pop) 가능
- queue: FIFO (First In First Out) - 가장 먼저 입력한 값부터 삭제 가능 (선착순 - 먼저 온 순서대로)
- dequeue: stack과 queue를 합친 상태 - 앞, 뒤로 삽입과 삭제가 가능
- linked list: 배열과 다르게 연속되지 않은 메모리에 저장되며, 현재 리스트가 다음 리스트에 대한 메모리 주소를 가지고 있음
               인덱스로 접근할 수 없기에, 인덱스 정보로 값을 알고자 한다면 더 오래 걸림
               하지만 배열이 가지지 못한 장점을 가짐
'''
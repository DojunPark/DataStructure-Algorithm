'''
stack은 LIFO (Last In First Out): 나중에 들어온 것이 먼저 나감 e.g., 동전 쌓기
queue는 FIFO (First In First Out): 먼저 들어온 것이 먼저 나감 e.g., 선착순

insert -> enqueue in queue (push in stack)
delete -> dequeue in queue (pop in stack)
'''

class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.front_index == len(self.items):
            print('Q is empty')
            return None
        else:
            x = self.items[self.front_index]
            self.front_index += 1
            return x


# Queue 실행
q = Queue()
q.enqueue(5)
q.enqueue(2)
q.enqueue(10)

print(q.dequeue())  # 5
print(q.dequeue())  # 2
print(q.dequeue())  # 10
print(q.dequeue())  # None


'''
Josephus problem
- n명의 사람 가운데 k번째 사람이 순차적으로 죽고 마지막 살아남은 한 사람을 return 하기
- Queue 자료구조를 사용하며, 죽지 않는 사람은 deque 후 즉시 enque를 함
- queue에 하나만 남을 때 까지 반복함
'''

def josephus(n, k):
    q = Queue()

    for i in range(1, n+1):
        q.enqueue(i)

    while q.front_index+1 < len(q.items):
        for i in range(1, k):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()

print('josephus 함수 실행')
print(josephus(6, 2))  # 6명 중 2번째 사람이 계속해서 죽을 경우, 마지막 생존자는 5
print(josephus(9, 3))  # 9명 중 3번째 사람이 계속해서 죽을 경우, 마지막 생존자는 1



'''
* dequeue
stack과 queue를 합친것
- 앞 뒤로 insert(append, appendleft), delete(pop, popleft)가 모두 가능함
- 파이썬에서 deque 내장 모듈을 제공함
'''

from collections import deque

dq = deque()

dq.appendleft(10)  # [10]
dq.append(0)       # [10, 0]
dq.appendleft(13)  # [13, 10, 0]
dq.append(3)       # [13, 10, 0, 3]

print('deque 출력')
print(dq)
print(dq.popleft())  # 13
print(dq.pop())      # 3
print(dq)            # [10, 0]
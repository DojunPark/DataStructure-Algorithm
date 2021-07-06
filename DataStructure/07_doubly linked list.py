'''
[doubly linked list]
- 양방향 연결 리스트의 node는 하나의 key, 두개의 link(next, prev)로 구성
- circular doubly linked list: head의 prev는 tail을 가리키고, tail의 next는 head를 가리킴
- dummy node: 원형 연결리스트의 시작을 나타내는 marker, None 값을 가짐
                      head와 tail의 link가 dummy node를 가리킴
                      dummy node를 head node라고 부름
'''

class Node:
    def __init__(self, key=None):
        self.key = key
        self.next= self
        self.prev = self
    def __str__(self):
        return str(self.key)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

d = DoublyLinkedList()






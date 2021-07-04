'''
[linked list]
- array와 다르게 linked list는 불연속적인 메모리에 값이 저장되고, key와 link가 하나의 node 구성
- 장점: insert 할때 linked list는 O(1)만큼 소요되며, array는 O(n)만큼 소요됨
- 단점: read 할때 array는 O(1)만큼 소요되는 반면, linked list는 O(n)만큼 소요됨
'''

'''
[singly vs. doubly linked list]
- singly: 왼쪽 -> 오른쪽 방향으로만 link가 있음 / key, link 하나씩
- doubly: 왼쪽 -> 오른쪽, 오른쪽 -> 왼쪽 모두 link가 있음 / key 하나, link 둘
'''

# 노드 클래스 선언
class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None  # 링크
    def __str__(self):
        return str(self.key)

# 노드 생성
a = Node(3)  # head node
b = Node(9)
c = Node(-1)

# 노드 연결
a.next = b
b.next = c


# 한방향 연결리스트 클래스 선언
# -> head node, 노드 개수 정보를 가짐
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # 빈 리스트
        self.size = 0

    def __len__(self):
        return self.size

    def pushFront(self, key):
        v = Node(key)
        v.next = self.head
        self.head = v
        self.size += 1

    def pushBack(self, key):
        v = Node(key)
        if len(self) == 0:
            self.head = v
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = v
        self.size += 1

    def popFront(self):
        if len(self) == 0:
            return None
        else:
            x = self.head
            key = x.key
            self.head = x.next  # 1. head 수정
            self.size -= 1  # 2. size 수정
            del x
            return key

    def popBack(self):
        if len(self) == 0:
            return None
        else:
            # running technique
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if len(self) == 1:
                self.head = None
            else:
                prev.next = tail.next  #None
                key = tail.key
                del tail
                self.size -= 1
                return key

    # generator -> for _ in _ 구문을 사용할 수 있게 함
    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next


# linked list 생성
l = SinglyLinkedList()

'''
pushFront와 popFront는 상수 시간 소요: O(1)
pushBack과 popBack은 선형적으로 증가하는 시간 소요: O(N)
'''

# 삽입
l.pushFront(1)  # 1 -> None
l.pushFront(9)  # 9 -> 1 -> None
l.pushFront(3)  # 3 -> 9 -> 1 -> None
l.pushBack(4)  # 3 -> 9 -> 1 -> 4 -> None

# 삭제
l.popFront()  # 9 -> 1 -> 4 -> None
l.popBack()  # 9 -> 1 -> None

# generator 실행
for i in l:
    print(i)


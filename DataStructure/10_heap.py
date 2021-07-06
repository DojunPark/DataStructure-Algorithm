'''
[Tree]
- 각 노드에는 키값을 가지고, 하나의 부모노드가 여러 자식 노드를 가짐
- 이진 트리(binary tree): 하나의 부모노드가 최대 두개까지의 자식 노드를 가지는 트리 구조
- 최상위 노드는 루트 노드(root node), 자식이 없는 최하단 노드를 리프 노드(leaf node)라고 함
- 링크(엣지): 노드와 노드를 연결하는 선
- 레벨(level): 최상위 노드가 속한 레벨이 0부터 시작하여 아래로 내려가며 1씩 증가
- 높이: 레벨 0부터 최고 레벨까지의 레벨 수
- 경로 길이: 엣지의 갯수

*표현법
ex1) A = [a, b, c, None, d, e, f, None, None, h, i, g]  # 리스트로 표현
ex2) A = [a, [b, [], [d, [], []], [c, [e, [], []], [f, [], []]]]  # 재귀적으로 리스트로 표현
ex3) node class로 표현


[heap]
- heap property를 만족하는 이진트리
- H[k]의 왼쪽 자식노드->H[k*2+1], H[k]의 오른쪽 자식노드->H[k*2+2]
- H[k]의 부모노드->H[(k-1)//2]
- 장점: 부모노드, 자식노드의 위치를 상수 시간 O(1)에 알 수 있음
- 단점: 빈 노드를 None으로 표시하기 위해 메모리가 낭비됨
- insert, find_max, delete_max 함수를 제공해야함

*heap property?
1. 왼쪽부터 차례대로 채운 이진 트리
2. 모든 부모노드의 key값은 자식 노드의 key값보다 크거나 같다
'''

class Heap:
    def __init__(self, L=[]):
        self.A = L
        self.make_heap()

    def __str__(self):
        return str(self.A)

    def heapify_down(k, n):
        while 2*K+1 < n:
            L, R = 2*k+1, 2*k+2
            if self.A[L] > self.A[k]:
                m = L
            else:
                m = k
            if R < n and self.A[R] > self.A[m]:
                m = R
            if m != k:
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m
            else:
                break

    def make_heap(self):
        n = len(self.A)
        for k in range(n-1, -1, -1):
            # A[k] -> heap property 만족하는 곳으로
           self.heapify_down(k, n)

    def heap_sort(self):
        n = len(self.A)
        for k in range(len(self.A)-1, -1, -1):
            self.A[0], self.A[k] = self.A[k], self.A[0]
            n = n-1
            self.heapify_down(0, n)

    def heapify_up(self, k):
        while k>0 and self.A[(k-1)//2] < self.A[k]
            self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
            k = (k-1)//2

    def insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A)-1)

    def delete_max(self):
        if len(self.A) == 0:
            return None
        key = self.A[0]
        self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
        self.A.pop()
        heapify_down(0, len(self.A))
        return key
'''
stack은 push(삽입)과 pop(삭제후 반환) 기능을 실행함
파이썬 list도 이에 해당하는 append와 pop을 제공하지만, 다른 기능이 사용될 수 있음으로,
본 연습에서는 stack class를 직접 만들어 볼 것
'''

class Stack:
    def __init__(self):
        self.items = []   # 데이터 저장을 위한 리스트 준비

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print('Stack is empty')  # pop할 아이템이 없으면 indexerror 발생

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print('Stack is empty')

    def __len__(self):          # len()로 호출하면 stack의 item 수 반환
        return len(self.items)


s = Stack()
s.push(1)
s.push(3)
s.push(5)

print(s.items)
print(s.pop())
print(s.top())
print(s.items)
print(len(s))

'''
문제 1: 괄호 맞추기
입력 - 왼쪽, 오른쪽 괄호가 포함된 문자열
출력 - 괄호 쌍이 맞춰져 있으면 true, 아니면 false
'''

# 입력 문자열

def varify(parseq):
    s = Stack()
    breaker = True

    for p in parseq:
        if p == '(':
            s.push(p)
        elif p == ')':
            if len(s) == 0:
                return False
            else:
                s.pop()
        else:
            breaker = False
            break

    if breaker == False:
        return 'The input sequence contains a not allowed symbol'
    elif len(s) > 0:
        return False
    else:
        return True

text1 = '(()())()0)'  # 기타 문자 포함
text2 = '(()())()'    # True
text3 = '(()())())('  # ( 추가
text4 = '(()())())'   # ) 추가

print(varify(text1))
print(varify(text2))
print(varify(text3))
print(varify(text4))


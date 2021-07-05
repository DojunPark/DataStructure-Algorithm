'''
[hash table]
- 상수 시간 O(1)의 삽입, 삭제, 탐색 연산이 가능함
- key, value로 구성된 데이터를 저장할 인덱스가 있는 hash table이 있음
- hash function을 거쳐 나온 값에 해당하는 index에 데이터를 저장함
- collision: slot에 이미 다른 데이터가 저장되어 있는 경우
- collision resolution method: collision을 피하여 데이터를 저장하는 방법
- slot의 갯수는 일반적으로 2의 제곱의 수로 구성되는 것이 일반적

[hash function]
- division hash function: 나눈 값의 나머지로 hash 값으로 이용
                                e.g., f(k) = k%m, f(k) = (k%p)%m  # m은 slot의 갯수
- perfect hash function: key값과 slot이 충돌 없이 one to one으로 매칭됨
                               이상적이나 현실적이지 않음
- universal hash function: 충돌할 확률이 1/m인 함수 -> 마찬가지로 설계하기 어려움
- c-universal hash function: 충돌할 확률이 c/m인 함수
- additive hash function: key값이 string인 경우, 문자의 ascii 코드 값을 모두 더해서 m으로 나눔
- 그 외에도 multiplication, folding, mid-squares, extraction, rotating hash function 등이 있음

* good hash function?
1. less collision
2. fast computation (collision과 trade-off 관계)

[collision resolution method]
- open addressing: collision이 일어났을 경우 다른 slot에 값을 저장하는 방법
- open addressing과 반대되는 방법으로 chaining 방법이 있음
- open addressing 방법에는 크게 linear probing, quadratic probing, double hashing이 있음

[linear probing]
- collision이 발생하였을 경우 한칸씩 밑으로 내려가면서 빈칸에 값을 저장함
- cluster(데이터를 가진 slot이 연속적으로 모여있는 경우) 때문에 연산 시간이 오래걸림
- search하는 경우 빈칸이 나올때까지 밑으로 내려가면서 탐색
- set의 경우 key값이 H에 있으면 value를 update, 없으면 (key, value)를 insert
- remove의 경우 key값을 가진 slot을 지우고 delete를 입력
'''


class HashOpenAddr:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None]*self.size
        self.values = [None]*self.size

    def find_slot(self, key):
        i = f(key)
        start = i
        while (H[i] == occupied) and (H[i].key != key):
            i = (i + 1) % m
            if 1 == start:
                return FULL
        return i

    def set(key, value=None):
        i = find_slot(key)
        if i == FULL:
            return None
        if H[i].is occupied:
            H[i].value = value
        else:
            H[i].key, H[i].value = key, value
        return key

    def remove(self, key):
        i = find_slot(key)
        if H[i] is unoccupied:
            return None
        j = i
        while True:
            while True:
                j = (j+1) % m
                if H[j] is unoccupied:
                    return key
                k = f(H[j].key)
                if not (i < k <= j or j<i<k or k<=j<i):
                    break

    def search(self, key):
        i = find_slot(key)
        if H[i] is occupied:
            return H[i].value
        else:
            return None

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        self.set(key, value)




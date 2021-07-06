# 시간 복잡도(time complexity) = worst case에 대한 기본연산 횟수
# 시간 복잡도가 일차식인 경우, n에 대하여 선형적으로(비례하여) 증가 / 이차식인 경우 n에 대해 제곱으로 증가
# 따라서, Big O notation은 함수의 증가율을 결정짓는 최고차항만으로 표기
# e.g., t1(n) = O(n) / t2(n) = O(n^2)

'''
계산 순서
1. 최고차항 n만 남긴다
2. 최고차항 n의 계수는 생략한다
3. O(최고차항 n) 으로 표기한다
'''

'''
수행시간이 상수항 밖에 없는 함수의 경우,
n^0 = 1
t3 = O(n^0) = O(1)
'''

def increment_one(n):
    return n+1


# 수행시간이 n보다 적게 증가하는 경우, O(log2^n)

def number_of_bits(n):
    count = 0
    while n > 0:
        n = n//2
        count += 1
    return count

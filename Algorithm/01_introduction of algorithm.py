# 최대공약수 계산하는 gcd 함수

def gcd_sub(a, b):
    n=0  # 실행횟수
    while a!=0 and b!=0:
        n+=1
        if a>b: a=a-b
        else: b=b-a
    return a+b, n

def gcd_mod(a, b):
    n=0  # 실행횟수
    while a!=0 and b!=0:
        n+=1
        if a>b: a=a%b
        else: b=b%a
    return a+b, n


# gcd_sub는 최대공약수를 얻기위해 큰수에서 작은수를 50번 반복하며 뺌
# 하지만 gcd_mod는 큰수에서 작은수를 나눈 몫을 계산하기에 1번만에 최대공약수를 얻을 수 있었음
print(gcd_sub(100, 2))
print(gcd_mod(100, 2))
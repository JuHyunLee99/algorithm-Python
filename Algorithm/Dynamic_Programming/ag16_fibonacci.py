# 이것이 코딩테스트이다
# 2023.12.03
# 피보나치 수열: 단순 재귀

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))
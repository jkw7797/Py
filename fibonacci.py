#재귀함수 사용
import sys
sys.setrecursionlimit(1000000)

s = {0: 0, 1: 1, } #memoization 사용

def fibo(n):
    if n in s:
        return s[n]
    else:
        output = fibo(n-1) + fibo(n-2)
        s[n] = output
        return output

for i in range(10):
    print(str(i)+"  :  "+ str(fibo(i)))

print("****************")
#초간단 피보
def fib(n):
    if n == 0 :
        return 0
    if n == 1:
        return 1
    return fib(n - 2)+fib(n - 1)

for i in range(10):
    print(str(i)+"  :  "+ str(fib(i)))
def fibo(n):
    if n==0 or n==1:
        return n
    return fibo(n-1)+fibo(n-2)

def fibo_series(n):
    for i in range(n):
        print(fibo(i), end=" ")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

fibo_series(5)
print()
print(factorial(5))

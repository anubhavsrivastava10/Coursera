def fibo(n):
    if n<=1:
        return n
    first = 0
    second = 1
    for i in range(n-1):
        first, second = second, first+second
    return second

n = int(input())
print(fibo(n))

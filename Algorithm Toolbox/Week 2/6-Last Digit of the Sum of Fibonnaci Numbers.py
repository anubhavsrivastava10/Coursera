def fibo(n):
    time_period = 60
    index = n % time_period
    #     print(index)
    if index < 1:
        return index
    prev, curr = 0, 1
    sum1 = 1
    for i in range(2, index + 1):
        prev, curr = curr, (curr + prev) % 10
        sum1 = (sum1 + curr) % 10
    return sum1


n = int(input())
print(fibo(n))
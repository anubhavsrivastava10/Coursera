def fibo(n, m):
    curr, prev = 1, 0
    time_period = 0
    for i in range(m * m + 1):
        prev, curr = curr, (curr + prev) % m
        if (prev, curr) == (0, 1):
            time_period = i + 1
            break

    index = n % time_period
    if index < 1:
        return index
    prev, curr = 0, 1
    for i in range(2, index + 1):
        prev, curr = curr, (curr + prev) % m
    return curr

n, m = map(int,input().split())
print(fibo(n,m))
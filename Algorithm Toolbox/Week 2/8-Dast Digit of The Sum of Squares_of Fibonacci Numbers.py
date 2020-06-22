def fibonacci(n):
    if n<2:
        return n
    prev,curr = 0,1
    for i in range(n-1):
        prev, curr = curr, (curr+prev)%10
    return curr

def sum_squares_period60():
    square_digits = [0] * 10
    for i in range(10):
        square_digits[i] = (i * i) % 10
    square_digits = dict(zip(list(range(10)), square_digits))
    summ = 0
    for i in range(60):
        summ = (summ + square_digits[fibonacci(i)]) % 10
    return summ


def fibonacci_squares(n):
    if n < 2:
        return n
    prev, curr, summ = 0, 1, 1
    num_time_periods = n // 60
    n %= 60
    square_digits = [0] * 10
    for i in range(10):
        square_digits[i] = (i * i) % 10
    square_digits = dict(zip(list(range(10)), square_digits))

    if n < 2:
        return (num_time_periods * sum_squares_period60() + n) % 10
    for i in range(n - 1):
        prev, curr = curr, (prev + curr) % 10
        summ = (summ + square_digits[curr]) % 10
    return (summ + num_time_periods * sum_squares_period60()) % 10


n = int(input())
print(fibonacci_squares(n))1
import sys
import math


def optimal_summands(n):
    summands = []
    # write your code here
    return summands


def max_num_prizes(n):
    numbers = []
    if n == 1:
        return [1]
    #     remaining = n
    else:
        m = 2 * int(math.sqrt(n)) + 1
        for i in range(1, m):
            if n > 2 * i:
                numbers.append(i)
                n -= i
        else:
            numbers.append(n)

    return numbers

input = sys.stdin.read()
n = int(input)
summands = max_num_prizes(n)
print(len(summands))
for x in summands:
    print(x, end=' ')
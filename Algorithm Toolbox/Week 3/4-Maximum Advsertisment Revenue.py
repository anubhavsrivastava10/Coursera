import sys
import numpy as np

def max_dot_product(a, b):
    a.sort()
    b.sort()
    a = np.array(a)
    b = np.array(b)
    res = int(sum(a * b))
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))

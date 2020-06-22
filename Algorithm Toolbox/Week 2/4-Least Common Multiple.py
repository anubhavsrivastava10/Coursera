def gcd(a, b):
    m = max(a, b)
    n = min(a, b)
    if m % n == 0:
        return n

    return gcd(n, m % n)


def lcm(a, b):
    n = min(a, b)
    if n == 0:
        return 0
    return int((a * b) / gcd(a, b))

a,b = map(int,input().split())
print(lcm(a,b))
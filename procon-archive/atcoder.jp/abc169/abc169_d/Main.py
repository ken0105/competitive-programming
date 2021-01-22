from collections import Counter

def prime_factorize(n):
    primes = []
    b = 2
    while b * b <= n:
        while n % b == 0:
            primes.append(b)
            n //= b
        b += 1
    if n > 1:
        primes.append(n)
    return primes


def count(n):
    cnt = 0
    total = 0
    while True:
        if n > total:
            cnt += 1
            total += cnt
        elif n == total:
            return cnt
        else:
            return cnt - 1


if __name__ == '__main__':
    n = int(input())
    c = Counter(prime_factorize(n))
    ans = 0
    for k in c:
        ans += count(c[k])
    print(ans)

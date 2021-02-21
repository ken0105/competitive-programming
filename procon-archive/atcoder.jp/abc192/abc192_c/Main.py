def g1(x):
    tmp = x[::]
    tmp.sort(reverse=True)
    return int("".join(tmp))

def g2(x):
    tmp = x[::]
    tmp.sort()
    return int("".join(tmp))

def f(x):
    return g1(x) - g2(x)

def main():
    n,k = map(int,input().split())
    x = list(str(n))
    for _ in range(k):
        x = f(x)
        x = list(str(x))
    print("".join(x))


if __name__ == '__main__':
    main()
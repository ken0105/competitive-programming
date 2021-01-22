import math

if __name__ == "__main__":
    base = set()
    for i in range(-150,150):
        base.add(i)
    x,n = map(int,input().split())
    target = set(map(int,input().split()))

    diff = base.difference(target)

    min = 0
    min_value = 1000
    diff = list(diff)
    for i in diff:
        if min_value > abs(i - x):
            min = i
            min_value = abs(i -x)
    print(min)

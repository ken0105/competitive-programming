if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a = a[::-1]
    b = b[::-1]
    a_before = sum(a)
    for i in range(len(b)):
        if a[i] <= b[i]:
            margin = b[i] - a[i]
            a[i] = 0
            b[i] = margin
        else:
            a[i] -= b[i]
            b[i] = 0

        if b[i] > 0 and i + 1 < len(a):
            if a[i+1] <= b[i]:
                margin = b[i] - a[i+1]
                a[i+1] = 0
                b[i] = margin
            else:
                a[i+1] -= b[i]
                b[i] = 0
    print(a_before - sum(a))
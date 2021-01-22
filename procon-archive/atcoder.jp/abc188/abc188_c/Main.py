if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    member = 2 ** n
    right = a[0:member//2]
    left = a[member//2:]
    second = min(max(right),max(left))
    print(a.index(second) + 1)
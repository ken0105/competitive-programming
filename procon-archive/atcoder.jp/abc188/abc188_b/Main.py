if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    x = 0
    for i in range(n):
        x += a[i] * b[i]
    if x == 0:
        print("Yes")
    else:
        print("No")
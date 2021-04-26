def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    fro = 0
    to = 10000
    for i in range(n):
        fro = max(a[i],fro)
        to = min(b[i],to)
    if to >= fro:
        print(to - fro + 1)
    else:
        print(0)
if __name__ == '__main__':
    main()

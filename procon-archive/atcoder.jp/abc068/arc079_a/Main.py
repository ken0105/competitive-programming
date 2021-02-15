def main():
    n,m = map(int,input().split())
    from_b = []
    from_a = []
    for _ in range(m):
        a,b = map(int,input().split())
        if a == 1:
            from_a.append(b)
        if b == n:
            from_b.append(a)
    from_b = set(from_b)
    for i in from_a:
        if i in from_b:
            print("POSSIBLE")
            exit()
    print("IMPOSSIBLE")

if __name__ == '__main__':
    main()
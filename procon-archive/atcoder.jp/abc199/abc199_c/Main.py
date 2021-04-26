def main():
    n = int(input())
    s = list(input())
    q = int(input())
    is_reverse = False
    for _ in range(q):
        t,a,b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 2:
            is_reverse = not is_reverse
        else:
            if is_reverse:
                if a >= n - 1:
                    a -= n
                elif a < n:
                    a += n
                if b >= n - 1:
                    b -= n
                elif b < n:
                    b += n
            s[a],s[b] = s[b], s[a]
    if is_reverse:
        print("".join(s[n:]+s[0:n]))
    else:
        print("".join(s))

if __name__ == '__main__':
    main()

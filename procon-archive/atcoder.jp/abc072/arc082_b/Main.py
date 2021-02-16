def main():
    n = int(input())
    p = list(map(int,input().split()))
    cnt = 0
    is_pass = False
    for i, num in enumerate(p):
        if i == n - 1 and i + 1 == num:
            cnt += 1
            break
        if i == n - 1:
            break
        if is_pass:
            is_pass = False
            continue
        if i + 1 == num:
            p[i + 1], p[i] = p[i], p[i + 1],
            cnt += 1
            is_pass = True
    print(cnt)

if __name__ == '__main__':
    main()
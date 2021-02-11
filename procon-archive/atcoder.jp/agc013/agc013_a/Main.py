if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    num_before = a[0]
    mode = 0
    for num in a:
        if num < num_before and mode == 1:
            ans += 1
            mode = 0
            num_before = num
            continue
        if num > num_before and mode == 2:
            ans += 1
            mode = 0
            num_before = num
            continue
        if mode == 0 and num > num_before:
            mode = 1
        elif mode == 0 and num < num_before:
            mode = 2
        num_before = num
        # print(mode)
    print(ans + 1)
1
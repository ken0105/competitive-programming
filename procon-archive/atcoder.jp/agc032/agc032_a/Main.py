def main():
    n = int(input())
    b = list(map(int,input().split()))
    ans = []
    while len(b) != 0:
        last_ope = -1
        for i,num in enumerate(b):
            if i + 1 == num:
                last_ope = i
        if last_ope == -1:
            print(-1)
            exit()
        ans.append(last_ope + 1)
        del b[last_ope]
    ans = ans[::-1]
    for i in ans:
        print(i)


if __name__ == '__main__':
    main()

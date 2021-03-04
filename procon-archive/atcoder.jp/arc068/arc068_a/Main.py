def main():
    x = int(input())
    cnt = x // (6 + 5) * 2
    x -= (6 + 5) * (cnt // 2)
    if x == 0:
        print(cnt)
        exit()
    if x <= 6:
        cnt += 1
    else:
        cnt += 2
    print(cnt)


if __name__ == '__main__':
    main()
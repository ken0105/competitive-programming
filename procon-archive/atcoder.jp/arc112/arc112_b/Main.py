def main():
    b,c = map(int,input().split())
    ans = (c-1) // 2 + (c-1) // 2 + (c // 2) + (max(0,c-2) // 2) + 2
    if b == 0 and c == 1:
        print(1)
        exit()

    if b > 0:
        situ1_from = b - (c // 2)
        situ2_to = -b + (c-1) // 2
    else:
        situ1_from = -b - (c-1)//2
        situ2_to = b + (c-2) // 2
    dupulicate = 0
    if situ1_from <= situ2_to:
        dupulicate = abs(situ2_to - situ1_from) + 1
    ans -= dupulicate

    print(ans)


if __name__ == '__main__':
    main()
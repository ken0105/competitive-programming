def main():
    global ans
    n = int(input())
    keta = len(str(n))
    commma1 = 999999 - 10 ** 3 + 1
    commma2 = (999999999 - 10 ** 6 + 1 ) * 2
    commma3 = (999999999999 - 10 ** 9 + 1) * 3
    commma4 = (999999999999999 - 10 ** 12 + 1) * 4
    if keta <= 3:
        print(0)
        exit()
    elif keta == 4 or keta == 5 or keta == 6:
        ans = n - 1000 + 1
    elif keta == 7 or keta == 8 or keta == 9:
        ans = commma1
        ans += (n - 10 ** 6 + 1) * 2
    elif keta == 10 or keta == 11 or keta == 12:
        ans = commma1 + commma2
        ans += (n - 10 ** 9 + 1) * 3
    elif keta == 13 or keta == 14 or keta == 15:
        ans = commma1 + commma2 + commma3
        ans += (n - 10 ** 12 + 1) * 4
    elif keta == 16:
        ans = commma1 + commma2 + commma3 + commma4 + 5
    print(ans)


if __name__ == '__main__':
    main()

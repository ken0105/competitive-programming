if __name__ == '__main__':
    n = int(input())
    s = input()
    t = input()
    ans = n * 2
    for i in range(n+1):
        if s[len(s) - i:] == t[0:i]:
            ans = n * 2 - i
    print(ans)
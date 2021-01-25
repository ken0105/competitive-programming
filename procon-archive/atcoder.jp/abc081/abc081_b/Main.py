if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    def __hasOdd(li):
        for l in li:
            if l % 2 == 1:
                return True
        return False

    while True:
        if not __hasOdd(a):
            ans += 1
        else:
            print(ans)
            exit()
        for i, num, in enumerate(a):
            a[i] = num // 2
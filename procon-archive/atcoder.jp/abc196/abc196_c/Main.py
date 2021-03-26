ans = 0
def main():
    n = int(input())
    k_2 = 1 * 9
    k_4 = 10 * 9
    k_6 = 100 * 9
    k_8 = 1000 * 9
    k_10 = 10000 * 9
    def calc(i):
        global ans
        num = int(str(i) + str(i))
        if num <= n:
            ans += 1
        else:
            raise ValueError

    try:
        for i in range(1,10):
            calc(i)
        for i in range(10,100):
            calc(i)
        for i in range(100,1000):
            calc(i)
        for i in range(1000,10000):
            calc(i)
        for i in range(10000,100000):
            calc(i)
        for i in range(100000,1000000):
            calc(i)
        for i in range(1000000,10000000):
            calc(i)
    except:
        print(ans)
        exit()


if __name__ == '__main__':
    main()

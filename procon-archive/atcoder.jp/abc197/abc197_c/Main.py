def main():
    n = int(input())
    a = list(map(int, input().split()))
    div = n - 1
    ALL = 1 << div
    ans = float('inf')
    for bit in range(ALL):
        l = []
        tmp = []
        for i,num, in enumerate(a):
            if bit >> i & 1:
                tmp.append(num)
                l.append(tmp)
                tmp = []
            else:
                tmp.append(num)
                if i == n - 1:
                    l.append(tmp)
        xors = []
        for i in l:
            xor = 0
            for j in i:
                xor |= j
            xors.append(xor)
        cnt = 0
        for i in xors:
            cnt ^= i
        ans = min(ans, cnt)
    print(ans)




if __name__ == '__main__':
    main()

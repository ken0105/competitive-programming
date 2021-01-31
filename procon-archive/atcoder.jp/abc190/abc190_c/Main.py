if __name__ == '__main__':
    n, m, = map(int, input().split())
    expects = []
    for i in range(m):
        a, b = map(int, input().split())
        expects.append((a,b))
    k = int(input())
    select = []
    for i in range(k):
        c, d = map(int, input().split())
        select.append((c,d))

    ans = 0

    for bit in range(2**k):
        cnt = 0
        dishes = set()
        for i in range(k):
            if bit >> i & 1:
                dishes.add(select[i][0])
            else:
                dishes.add(select[i][1])
        for a,b in expects:
            if a in dishes and b in dishes:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)


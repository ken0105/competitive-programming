def main():
    n = int(input())
    l = [[] for _ in range(n)]
    for _ in range(n):
        x,c = map(int, input().split())
        l[c-1].append(x)

    color = 0
    for i in l:
        if len(i) != 0:
            color += 1

    right = 0
    left = 0
    dpr = 0
    dpl = 0
    for i in l:
        if len(i) == 0:
            continue
        i.sort()
        dpl_next = min(dpr + abs(i[-1] - right), dpl + abs(i[-1] - left)) + abs(i[0] - i[-1])
        dpr_next = min(dpr + abs(i[0] - right), dpl + abs(i[0] - left)) + abs(i[0] - i[-1])
        right = i[-1]
        left = i[0]
        dpl = dpl_next
        dpr = dpr_next
    ans = min(abs(right) + dpr, abs(left) + dpl)
    print(ans)




if __name__ == '__main__':
    main()

from collections import defaultdict


def main():
    n,x = map(int, input().split())
    wa,wb = [],[],
    for i in range(n):
        if i % 2 == 0:
            wa.append(int(input()))
        else:
            wb.append(int(input()))

    dic = defaultdict(int)
    for i in range(1 << len(wa)):
        a_total = 0
        for j in range(len(wa)):
            if i >> j & 1:
                a_total += wa[j]
        dic[a_total] += 1

    ans = 0
    for i in range(1 << len(wb)):
        b_total = 0
        for j in range(len(wb)):
            if i >> j & 1:
                b_total += wb[j]
        ans += dic[x - b_total]
    print(ans)


if __name__ == '__main__':
    main()

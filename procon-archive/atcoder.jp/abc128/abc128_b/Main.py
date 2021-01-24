import itertools

if __name__ == '__main__':
    n = int(input())
    d = []
    for i in range(1, n + 1):
        s, p = map(str, input().split())
        d.append([i, s, int(p)])
    sorted_d = sorted(d, key=lambda x: (x[1], -x[2]))

    for s in sorted_d:
        print(s[0])
import itertools

def main():
    s = input()
    k = int(input())
    group = [len(list(g)) for c,g in itertools.groupby(s)]
    ans = sum(list(map(lambda g: g // 2, group))) * k
    if len(group) == 1:
        print(len(s) * k // 2)
        exit()
    if s[0] == s[-1] and group[0] % 2 == 1 and group[-1] % 2 == 1:
        ans += k - 1
    print(ans)

if __name__ == '__main__':
    main()

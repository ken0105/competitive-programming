import itertools
from collections import Counter


def main():
    n = int(input())
    s = input()
    cnt_s = Counter(s)
    ans = 1
    for num in cnt_s.values():
        ans = ans * (num + 1)
    print((ans - 1) % (10 ** 9 + 7))

if __name__ == '__main__':
    main()

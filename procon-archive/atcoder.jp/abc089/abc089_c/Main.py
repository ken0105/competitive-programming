import itertools
import math
from collections import Counter


def main():
    n = int(input())
    s = []
    for _ in range(n):
        t = input()[0]
        if t in ["M", "A", "R", "C", "H"]:
            s.append(t)
    cnt_s = Counter(s)
    ans = 0
    for a,b,c in itertools.combinations(cnt_s.keys(), 3):
        ans += cnt_s[a] * cnt_s[b] * cnt_s[c]
    print(ans)


if __name__ == '__main__':
    main()
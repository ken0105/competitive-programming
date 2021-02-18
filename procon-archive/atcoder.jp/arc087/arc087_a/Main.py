import math
from collections import Counter


def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt_a = Counter(a)
    ans = 0
    for i in cnt_a.keys():
        if i != cnt_a[i]:
            del_pattern = cnt_a[i]
            if del_pattern > i:
                ans += del_pattern - i
            else:
                ans += del_pattern
    print(ans)


if __name__ == '__main__':
    main()
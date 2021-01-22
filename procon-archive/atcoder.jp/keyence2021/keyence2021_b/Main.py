import itertools
import math
from collections import Counter

if __name__ == '__main__':
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a_cnt = Counter(a)
    max_t = []
    a_keys = set(a_cnt.keys())
    # a_keys.sort()
    max_a = max(a_cnt.keys())
    rest = k
    # print(a_cnt)
    ans = 0
    for key in range(max(a_keys)+1):
        if key not in a_keys:
            a_cnt[key] = 0
    #     if rest > a_cnt[key]:
    #         for _ in range(rest - a_cnt[key]):
    #             max_t.append(key)
    #         rest -= a_cnt[key]
    # print(max_t)
    # if len(max_t) != k:
    #     print(sum(max_t) + (max_a + 1))
    # else:
    #     print(sum(max_t))
        if rest == 0:
            print(ans)
            exit()
        if a_cnt[key] >= rest:
           ans += 1 * rest
        else:
            rest = a_cnt[key]
            ans += 1 * rest
    print(ans)





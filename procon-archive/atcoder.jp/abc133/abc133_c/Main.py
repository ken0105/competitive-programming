import itertools
import math

if __name__ == '__main__':
    l, r = map(int, input().split())
    margin = r - l
    loop = 2019
    if margin < 2019:
        loop = margin

    ans = float('inf')
    for i in range(loop):
        for j in range(i + 1, loop+1):
            if l + j <= r:
                ans = min(ans, (l + i) * (l + j) % 2019)
    print(ans)
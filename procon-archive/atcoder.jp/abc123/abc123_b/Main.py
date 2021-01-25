import itertools
import math
import re

if __name__ == '__main__':
    l = []
    for i in range(5):
        l.append(int(input()))

    ans = float('inf')
    for a,b,c,d,e in itertools.permutations(l,5):
        time = 0
        time += math.ceil(a/10) * 10
        time += math.ceil(b/10) * 10
        time += math.ceil(c/10) * 10
        time += math.ceil(d/10) * 10
        time += e
        ans = min(ans, time)
    print(ans)

import itertools
from collections import Counter

if __name__ == '__main__':
    l = list(map(int,input().split()))
    ans = float('inf')
    for a,b in itertools.combinations(l,2):
        ans = min(ans, a+b)
    print(ans)
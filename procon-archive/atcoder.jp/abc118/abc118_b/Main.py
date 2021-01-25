import itertools
import math
import re

if __name__ == '__main__':
    n, m = map(int,input().split())
    fav = []
    for i in range(n):
        k, *a = map(int,input().split())
        if i == 0:
            a = [*a]
            fav = set(a)
            continue
        a = set([*a])
        fav = fav.intersection(a)
    print(len(fav))

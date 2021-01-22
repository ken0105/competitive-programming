# import math
# from decimal import *
import numpy as np

# from collections import deque, Counter
import itertools
# import sys
# import collections

if __name__ == '__main__':
    n,m = map(int, input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    songs = list(itertools.permutations(list(range(m)),2))
    score_max = 0
    for x,y in songs:
        score = 0
        for i in a:
            score += max(i[x], i[y])
        score_max = max(score_max, score)
    print(score_max)

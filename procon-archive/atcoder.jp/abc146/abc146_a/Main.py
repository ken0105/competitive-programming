import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools

if __name__ == '__main__':
    s = input()
    d = {"MON": 2, "TUE": 3, "WED": 4, "THU": 5, "FRI": 6, "SAT": 7, "SUN": 1}
    print(8 - d[s])

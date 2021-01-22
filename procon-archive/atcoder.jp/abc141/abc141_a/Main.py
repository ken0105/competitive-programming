import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools

if __name__ == '__main__':
    s = input()
    if 'Sunny' == s:
        print("Cloudy")
    elif 'Cloudy' == s:
        print("Rainy")
    else:
        print("Sunny")

import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools


def is_prime(num):
    for i in range(2, math.ceil(math.sqrt(num))):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    x = int(input())
    for i in range(x, 100000000000000):
        if is_prime(i):
            print(i)
            exit()


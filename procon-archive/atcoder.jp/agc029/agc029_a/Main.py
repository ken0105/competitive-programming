import math
from collections import deque

if __name__ == '__main__':
    s = input()
    left = 0
    ans = 0
    for i,color in enumerate(s):
        if color == "W":
            ans += (i - left)
            left += 1
    print(ans)

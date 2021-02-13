from collections import deque, Counter
from itertools import permutations


def main():
    s = list(input())

    up = set()
    down = set()
    for index, direct in enumerate(s):
        if direct == "U":
            up.add(index + 1)
        else:
            down.add(index + 1)
    stairs = [i for i in range(1,len(s) + 1)]
    ans = 0
    for stair in stairs:
        if stair in up:
            ans += len(stairs) - stair
            ans += (stair - 1) * 2
        else:
            ans += stair - 1
            ans += (len(stairs) - stair) * 2
    print(ans)


if __name__ == '__main__':
    main()
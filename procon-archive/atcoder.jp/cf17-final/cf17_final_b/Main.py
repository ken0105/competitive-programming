from collections import deque, Counter
from itertools import permutations


def main():
    s = input()
    s_count = list(Counter(s).values())
    if len(s_count) < 3 and max(s_count) >= 2:
        print("NO")
        exit()
    if max(s_count) - min(s_count) >= 2:
        print("NO")
        exit()
    print("YES")


if __name__ == '__main__':
    main()
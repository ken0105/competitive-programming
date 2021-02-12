from math import ceil

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    min_index = a.index(1)
    #
    # ans = float('inf')
    # left = min_index + 1
    # right = len(a) - min_index
    # left_cnt = ceil(((left - k) / (k - 1))) + 1
    # righ_cnt = ceil(((right - k) / (k - 1))) + 1
    #
    # if min_index == 0:
    #     left_cnt = 0
    # if min_index == len(a) - 1:
    #     righ_cnt = 0
    #
    # cnt = left_cnt + righ_cnt
    # ans = min(ans, cnt)
    # print(int(cnt))
    print(ceil((n - k) / (k - 1) + 1))
from itertools import permutations

if __name__ == '__main__':
    n = int(input())
    p = tuple(map(int,input().split()))
    q = tuple(map(int,input().split()))

    nums = [i for i in range(1,n+1)]
    p_order = 0
    q_order = 0
    cnt = 0
    for i in permutations(nums, n):
        cnt += 1
        if i == p:
            p_order = cnt
        if i == q:
            q_order = cnt
    print(abs(p_order - q_order))

import itertools

if __name__ == '__main__':
    n = int(input())
    W = list(map(int,input().split()))
    half_sum_W = sum(W) / 2
    s = 0
    after = 0
    before = 0
    for w in W:
        if s + w == half_sum_W:
            print(0)
            exit()
        elif s + w > half_sum_W:
            after = s + w
            before = s
            break
        else:
            s += w
    ans = min(abs(after - half_sum_W) * 2, abs(before - half_sum_W) * 2)
    print(int(ans))
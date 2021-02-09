from collections import Counter

if __name__ == '__main__':
    N,T = map(int,input().split())
    ts = list(map(int,input().split()))
    total = 0
    for i,t in enumerate(ts):
        if i == len(ts) - 1:
            total += T
            continue
        total += min(T, ts[i+1] - t)
    print(total)



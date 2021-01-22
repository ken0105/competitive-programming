from itertools import accumulate

if __name__ == '__main__':
    n,k = map(int,input().split())
    p = [0] + list(map(int,input().split()))
    for i in range(len(p)):
        p[i] = (1+p[i])*p[i]/2/(p[i] or 1)
    p_ac = list(accumulate(p))
    ans = 0
    for i in range(len(p_ac)):
        if i + k < len(p_ac):
           ans = max(ans,p_ac[i+k] - p_ac[i])
    print(ans)
if __name__ == '__main__':
    n = int(input())
    t,a = map(int,input().split())
    h = list(map(int,input().split()))
    diff_temp = float('inf')
    ans = 0
    for i, height in enumerate(h):
        temp = t - height * 0.006
        if diff_temp > abs(temp - a):
            ans = i + 1
            diff_temp = abs(temp -a)
    print(ans)

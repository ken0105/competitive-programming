from collections import Counter

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    cnt_a = Counter(a)
    ans = 0
    for i in range(10**5):
        ans = max(ans, cnt_a[i] + cnt_a[i+1] + cnt_a[i+2])
    print(ans)
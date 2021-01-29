from collections import Counter

if __name__ == '__main__':
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    m = int(input())
    for i in range(m):
        t.append(input())
    cnt_s = Counter(s)

    ans = 0
    for i, string in enumerate(cnt_s):
        ans = max(ans,cnt_s[string] - t.count(string))
    print(ans)
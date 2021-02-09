from collections import Counter

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a_cnt = Counter(a)
    a_type = list(a_cnt.values())
    a_type.sort(reverse=True)

    ans = 0
    while len(a_type) > k:
        ans += a_type.pop()

    print(ans)

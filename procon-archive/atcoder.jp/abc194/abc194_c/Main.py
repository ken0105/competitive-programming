from collections import Counter


def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt_a = Counter(a)
    set_a = set(a)
    a = list(set_a)
    ans = 0
    for i in range(len(set_a)):
        for j in range(i, len(set_a)):
            ans += abs(a[i] - a[j]) ** 2 * (cnt_a[a[i]] * cnt_a[a[j]])
    print(ans)


if __name__ == '__main__':
    main()

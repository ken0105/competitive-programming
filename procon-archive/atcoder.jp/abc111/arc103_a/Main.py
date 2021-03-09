from collections import Counter


def main():
    n = int(input())
    v = list(map(int, input().split()))
    odd_v = v[0::2]
    even_v = v[1::2]
    cnt_odd = Counter(odd_v)
    cnt_odd = sorted(cnt_odd.items(), key=lambda x:x[1], reverse=True)
    ans_odd = n // 2 - cnt_odd[0][1]
    cnt_even = Counter(even_v)
    cnt_even = sorted(cnt_even.items(), key=lambda x:x[1], reverse=True)
    ans_even = n // 2 - cnt_even[0][1]
    if cnt_odd[0][0] == cnt_even[0][0]:
        if len(cnt_odd) == 1 and len(cnt_even) == 1:
            ans = n // 2
            print(ans)
            exit()
        elif len(cnt_odd) == 1:
            ans_even = n // 2 - cnt_even[1][1]
        elif len(cnt_even) == 1:
            ans_odd = n // 2 - cnt_odd[1][1]
        else:
            if cnt_odd[1][1] > cnt_even[1][1]:
                ans_odd = n //2 - cnt_odd[1][1]
            else:
                ans_even = n // 2 - cnt_even[1][1]

    print(ans_even + ans_odd)


if __name__ == '__main__':
    main()

import math


def main():
    n = int(input())
    c = [float('inf')] + list(map(int, input().split()))
    q = int(input())
    all_min = min(c)
    odd_min = min(c[1::2])
    total_minus = 0
    odd_minus = 0
    total = 0
    for _ in range(q):
        command, *li = map(int, input().split())
        if command == 1:
            rest = c[li[0]] - li[1] - total_minus
            is_odd = li[0] % 2 == 1
            if is_odd:
                rest -= odd_minus
            if rest >= 0:
                total += li[1]
                c[li[0]] = c[li[0]] - li[1]
                if rest < all_min:
                    all_min = rest
                if is_odd and rest < odd_min:
                    odd_min = rest
        elif command == 2:
            rest = odd_min - li[0]
            if rest >= 0:
                odd_min = rest
                total += li[0] * math.ceil(n / 2)
                odd_minus += li[0]
            if all_min > odd_min:
                all_min = odd_min
        else:
            rest = all_min - li[0]
            if rest >= 0:
                all_min = rest
                odd_min = odd_min - li[0]
                total += li[0] * n
                total_minus += li[0]
    print(total)

if __name__ == '__main__':
    main()

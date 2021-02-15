from collections import Counter


def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt_a = Counter(a)
    hen = []
    squere = []
    for i in cnt_a.keys():
        if cnt_a[i] >= 2:
            hen.append(i)
        if cnt_a[i] >= 4:
            squere.append(i)
    hen.sort(reverse=True)
    squere.sort(reverse=True)
    if len(hen) < 2:
        print(0)
        exit()
    candidate = 0
    if squere:
        candidate = squere[0] ** 2
    print(max(hen[0] * hen[1], candidate))


if __name__ == '__main__':
    main()
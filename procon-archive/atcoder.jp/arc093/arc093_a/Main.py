from collections import Counter


def main():
    n = int(input())
    a = [0] + list(map(int, input().split())) + [0]
    total = 0
    for index, num in enumerate(a):
        if index == len(a) - 1:
            continue
        total += abs(a[index + 1] - a[index])

    for index, num in enumerate(a):
        if index == 0 or index == len(a) - 1:
            continue
        pre_dist = abs(a[index + 1] - a[index]) + abs(a[index] - a[index -1])
        new_dist = abs(a[index + 1] - a[index - 1])
        print(total - abs(new_dist - pre_dist))


if __name__ == '__main__':
    main()
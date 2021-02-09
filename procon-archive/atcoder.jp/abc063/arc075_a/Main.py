from collections import Counter

if __name__ == '__main__':
    N = int(input())
    s = [int(input()) for i in range(N)]

    sum_s = sum(s)
    not_10 = []
    if sum_s % 10 != 0:
        print(sum_s)
        exit()

    for num in s:
        if num % 10 != 0:
            not_10.append(num)
    not_10.sort()
    if len(not_10) == 0:
        print(0)
        exit()

    print(sum_s - not_10[0])




import math

if __name__ == "__main__":
    n = int(input())

    sum1, sq, max1 = 0, 0, 0;

    li = list(map(int, input().split()))

    for i in range(n):
        i = abs(li[i])
        sum1 += i
        sq += i ** 2
        if max1 < i:
            max1 = i
    sq = math.sqrt(sq)
    print(sum1)
    print(sq)
    print(max1)



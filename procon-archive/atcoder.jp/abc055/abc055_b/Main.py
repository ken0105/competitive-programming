from collections import Counter

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n):
        n = n * i % (10 ** 9 + 7)
    print(n)
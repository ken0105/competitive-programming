from collections import Counter

if __name__ == '__main__':
    n = int(input())
    a = set()
    for _ in range(n):
        num = int(input())
        if num in a:
            a.remove(num)
        else:
            a.add(num)
    print(len(a))
from collections import deque

if __name__ == '__main__':
    x = int(input())
    amari = x % 100
    syo = x // 100
    if syo * 5 < amari:
        print(0)
    else:
        print(1)




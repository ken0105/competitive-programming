from collections import deque


def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = deque()
    for i,num in enumerate(a):
        if (i + 1) % 2 == 0:
            b.appendleft(num)
        else:
            b.append(num)

    if n % 2 == 0:
        print(*b)
    else:
        b = list(b)
        b.reverse()
        print(*b)



if __name__ == '__main__':
    main()

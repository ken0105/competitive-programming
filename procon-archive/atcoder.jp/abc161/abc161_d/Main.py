from collections import deque


def main():
    k = int(input())
    queue = deque()
    n = 0
    if k <= 9:
        print(k)
        exit()
    for i in range(1,10):
        queue.append(i)
        n += 1
    while queue:
        num = queue.popleft()
        if n == k:
            print(queue.pop())
            break
        for i in range(0,10):
            if abs(int(str(num)[-1]) - i) <= 1:
                n += 1
                if n == k:
                    print(num * 10 + i)
                    exit()
                queue.append(num * 10 + i)




if __name__ == '__main__':
    main()

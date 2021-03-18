from collections import deque


def main():
    n = int(input())
    ans = 0
    queue = deque()
    queue.append(0)
    while queue:
        num = queue.popleft()
        if num > n:
            continue
        if "3" in str(num) and "5" in str(num) and "7" in str(num):
            ans += 1
        queue.append(10 * num + 3)
        queue.append(10 * num + 5)
        queue.append(10 * num + 7)
    print(ans)



if __name__ == '__main__':
    main()

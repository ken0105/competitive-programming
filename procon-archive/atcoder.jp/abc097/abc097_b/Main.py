from collections import deque

if __name__ == '__main__':
    x = int(input())
    ans = 0
    for i in range(1,40):
        for j in range(2,40):
            if i ** j > x:
                break
            ans = max(ans, i ** j)
    print(ans)

from collections import deque

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    ans = 0
    cnt = 0
    for i,num, in enumerate(a):
        if cnt == n:
            break
        if (i + 1) % 2 == 0:
            ans += num
            cnt += 1
    print(ans)

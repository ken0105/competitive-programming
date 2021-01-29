from collections import deque

if __name__ == '__main__':
    n,a,b = map(int,input().split())
    ans = float('inf')
    if abs(b-a) % 2 == 0:
        ans = abs(b-a) //2

    left = a-1
    b_moved = b - left
    if b_moved % 2 == 0:
        dist = left + 1
    else:
        dist = left
    dist += (b_moved - 1) // 2
    ans = min(dist, ans)
    right = n - b
    a_moved = a + right
    if abs(a_moved - n) % 2 == 0:
        dist = right
    else:
        dist = right + 1
    dist += (n - a_moved) // 2
    ans = min(dist,ans)

    print(ans)
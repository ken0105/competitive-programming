from collections import deque

if __name__ == '__main__':
    nums = list(map(int,input().split()))
    nums.sort()
    a = nums[0]
    b = nums[1]
    c = nums[2]

    ans = 0
    first = c - b
    if (c - a - first) % 2 == 0:
        ans += (c-a - first) // 2 + first
    else:
        ans += (c-a - first) // 2 + first + 2
    print(ans)



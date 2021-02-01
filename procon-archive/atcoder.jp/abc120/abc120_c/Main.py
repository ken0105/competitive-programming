from collections import deque

if __name__ == '__main__':
    s = input()
    buffer = deque()
    ans = 0
    for i, num in enumerate(s):
        if len(buffer) == 0:
            buffer.append(num)
            continue

        if buffer[-1] != num:
            buffer.popleft()
            ans += 2
        else:
            buffer.append(num)
    print(ans)



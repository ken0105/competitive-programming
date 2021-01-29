from collections import deque

if __name__ == '__main__':
    n = input()
    ans = 0
    ans2 = 0
    for i in n:
        ans += int(i)
    if n.startswith("1"):
        for i in n[1:]:
            ans2 += 9
        ans = max(ans,ans2)
    else:
        ans2 = int(n[0]) - 1
        for i in n[1:]:
            ans2 += 9
        ans = max(ans,ans2)
    print(ans)


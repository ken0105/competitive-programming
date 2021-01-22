from collections import deque
if __name__ == '__main__':
    s = input()
    query_cnt = int(input())
    ans = deque()
    ans.append(s)
    is_reverse = False
    for _ in range(query_cnt):
        l = list(map(str, input().split()))
        if l[0] == "1":
            is_reverse = not is_reverse
        else:
            if l[1] == "1" and not is_reverse:
                ans.appendleft(l[2])
            elif l[1] == "1" and is_reverse:
                ans.append(l[2])
            elif l[1] == "2" and not is_reverse:
                ans.append(l[2])
            elif l[1] == "2" and is_reverse:
                ans.appendleft(l[2])

    a = ""
    if is_reverse:
        for i in range(len(ans)-1,-1,-1):
            a += ans[i][::-1]
    else:
        for i in ans:
            a += i
    print(a)
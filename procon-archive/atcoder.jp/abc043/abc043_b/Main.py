from collections import deque

if __name__ == '__main__':
    s = input()
    queue = deque()
    for i in s:
        if i == "0":
            queue.append("0")
        elif i == "1":
            queue.append("1")
        else:
            try:
                queue.pop()
            except:
                pass
    ans = ""
    for i in list(queue):
        ans += i
    print(ans)
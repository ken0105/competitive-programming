from collections import deque


def main():
    s = input()
    t = deque()
    is_reverse = False
    for c in s:
        if c == "R":
            is_reverse = not is_reverse

        else:
            if len(t) == 0:
                t.append(c)
            elif is_reverse:
                if t[0] != c:
                    t.appendleft(c)
                else:
                    t.popleft()
            else:
                if t[-1] != c:
                    t.append(c)
                else:
                    t.pop()

    ans = "".join(t)
    if is_reverse:
        print(ans[::-1])
    else:
        print(ans)
if __name__ == '__main__':
    main()

from collections import deque

if __name__ == '__main__':
    s = input()
    seen = []
    temp = ""
    for i, c in enumerate(s):
        temp += c
        if len(seen) == 0 or temp != seen[-1]:
            seen.append(temp)
            temp = ""
    print(len(seen))





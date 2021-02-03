if __name__ == '__main__':
    s = input()
    l = [0] * (len(s) + 1)
    for i, symbol in enumerate(s):
        if symbol == "<":
            l[i + 1] = max(l[i] + 1, l[i + 1])

    for i in range(len(l) - 2, -1, -1):
        if s[i] == ">":
            l[i] = max(l[i + 1] + 1, l[i])
    print(sum(l))
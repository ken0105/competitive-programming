def add_chr(string, seen):
    for i in range(26):
        c = chr(ord('a') + i)
        if c not in seen:
            return string + c

def main():
    s = input()
    set_s = set(s)
    if len(set_s) != 26:
        print(add_chr(s, set(s)))
        exit()

    if s == "zyxwvutsrqponmlkjihgfedcba":
        print(-1)
        exit()

    for i in range(1,len(s) +1):
        trim = s[len(s) - i:]
        # print(trim)
        target = trim[0]
        candidate = []
        is_changed = False
        for c in trim:
            if c > target:
                is_changed = True
                candidate.append(c)
        candidate.sort()
        if is_changed:
            print(s[:len(s) - i] + candidate[0])
            exit()


if __name__ == '__main__':
    main()

if __name__ == '__main__':
    s = input()
    t = input()

    for i in range(len(s)):
        s = s[-1] + s[0:-1]
        if s == t:
            print("Yes")
            exit()
    print("No")
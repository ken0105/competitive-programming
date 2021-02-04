if __name__ == '__main__':
    s = input()
    for i in range(len(s)):
        s = s[0:-1]
        if len(s) % 2 == 0 and s[0:len(s)//2] * 2 == s:
            print(len(s))
            exit()

if __name__ == '__main__':
    n = int(input())
    s = input()
    tmp = ""
    slime = []
    for i in range(n):
        if tmp != s[i]:
            tmp = s[i]
            slime.append(s[i])
    print(len(slime))
if __name__ == '__main__':
    n = int(input())
    s = input()
    ans = 0
    now = 0
    for i in s:
        if i == "I":
            now += 1
        else:
            now -= 1
        ans = max(ans,now)
    print(ans)
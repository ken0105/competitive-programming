def main():
    s = list(input())
    tmp_s = s[::]
    chars = list(set(s))
    ans = float('inf')
    if len(set(tmp_s)) == 1:
        print(0)
        exit()
    for i in chars:
        cnt = 0
        tmp_s = s[::]
        while True:
            for j in range(1,len(tmp_s)):
                if tmp_s[j] == i:
                    tmp_s[j-1] = i
            cnt += 1
            tmp_s = tmp_s[0:-1]
            if len(set(tmp_s)) == 1:
                break
        ans = min(cnt,ans)
    print(ans)

if __name__ == '__main__':
    main()
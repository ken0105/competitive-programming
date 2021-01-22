if __name__ == "__main__":
    h,w,k = map(int,input().split())
    li = []
    ans = 0
    for i in range(h):
        li.append(input())

    for row in range(1 << h):
        for col in range(1 << w):
            count = 0
            for i in range(h):
                for j in range(w):
                    if row >> i & 1 == 1:
                        continue
                    if col >> j & 1 == 1:
                        continue
                    if li[i][j] == '#':
                        count += 1
            if count == k:
                ans += 1
    print(ans)




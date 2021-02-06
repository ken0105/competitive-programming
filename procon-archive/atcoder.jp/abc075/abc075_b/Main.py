if __name__ == '__main__':
    H,W = map(int,input().split())
    S = []
    for i in range(H):
        S.append(input())
    bom = set()

    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                bom.add((i,j))

    ans = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            for k in range(-1,2):
                for l in range(-1,2):
                    if S[i][j] == "#":
                        ans[i][j] = "#"
                        continue
                    try:
                        if i+k >=0 and j+l >= 0 and S[i+k][j+l] == "#":
                            ans[i][j] += 1
                    except:
                        pass

    for i in range(H):
        for j in range(W):
            if j != W-1:
                print(ans[i][j], end="")
            else:
                print(ans[i][j])

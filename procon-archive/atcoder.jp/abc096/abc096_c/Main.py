from collections import Counter

if __name__ == '__main__':
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                if (i-1 >= 0 and s[i-1][j] == ".")\
                        and (j-1 >= 0 and s[i][j-1] == ".")\
                        and (i+1 <h and s[i+1][j] == ".")\
                        and (j+1 < w and s[i][j+1] == ".")\
                        :
                    print("No")
                    exit()
    print("Yes")
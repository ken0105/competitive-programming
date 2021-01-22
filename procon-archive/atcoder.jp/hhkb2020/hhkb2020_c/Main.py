if __name__ == "__main__":
    n = int(input())
    li = list(map(int, input().split()))
    ar = [False] * 200010
    ans = 0
    for i in range(n):
        index = li[i]
        ar[index] = True
        while ar[ans] == True:
            ans += 1
        print(ans)





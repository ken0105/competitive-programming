if __name__ == "__main__":
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        stri = str(i)
        if len(stri) % 2 == 1:
            ans += 1
    print(ans)
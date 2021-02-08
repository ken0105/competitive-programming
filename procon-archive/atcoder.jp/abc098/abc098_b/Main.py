if __name__ == '__main__':
    N = int(input())
    S = input()
    ans = 0
    for i in range(1,N):
        f = set(S[0:i])
        e = set(S[i:])
        ans = max(ans, len(f.intersection(e)))
    print(ans)

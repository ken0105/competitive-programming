if __name__ == "__main__":
    n = int(input())
    p = list(map(int,input().split()))
    sorted_p = p[:]
    sorted_p.sort()
    cnt = 0
    for i in range(len(p)):
        if sorted_p[i] != p[i]:
            cnt += 1
    if cnt == 2 or cnt == 0:
        print("YES")
    else:
        print("NO")
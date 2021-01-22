if __name__ == "__main__":
    n = int(input())
    h = list(map(int, input().split()))
    for i in range(len(h)):
        if i - 1 < 0:
            continue

        if h[i] >= h[i - 1] + 1:
            h[i] -= 1
        elif h[i] == h[i - 1]:
            pass
        else:
            print("No")
            exit()
    print("Yes")
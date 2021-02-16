def main():
    n,a,b,c,d = map(int,input().split())
    road = ["."] + list(input())
    goal = max(c,d)
    for i in range(a,goal + 1):
        if i + 1 > n - 1:
            break
        if road[i] == "#" and road[i + 1] == "#":
            print("No")
            exit()

    if c > d:
        is_ok = False
        for i in range(b - 1, d):
            if i + 2 > n - 1:
                break
            if road[i] == "." and road[i + 1] == "." and road[i + 2] == ".":
                is_ok = True
                break
        if not is_ok:
            print("No")
            exit()

    print("Yes")
    exit()




if __name__ == '__main__':
    main()
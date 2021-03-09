def main():
    n, q = map(int, input().split())
    f_list = [["N"] * (n + 1) for _ in range(n + 1)]
    for _ in range(q):
        command, *li, = map(int, input().split())
        solve(n, f_list, command, li)
    for i,row in enumerate(f_list):
        if i == 0:
            continue
        row[i] = "N"
        print("".join(row[1:]))

def solve(n, f_list, command, li):
    if command == 1:
        f_list[li[0]][li[1]] = "Y"
    elif command == 2:
        for i in range(n+1):
            if f_list[i][li[0]] == "Y":
                f_list[li[0]][i] = "Y"
    else:
        follow_list = []
        for i in range(n+1):
            if f_list[li[0]][i] == "Y":
                follow_list.append(i)
        for i in follow_list:
            for j in range(n+1):
                if f_list[i][j] == "Y":
                    f_list[li[0]][j] = "Y"


if __name__ == '__main__':
    main()

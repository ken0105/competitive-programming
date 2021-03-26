def main():
    n = int(input())
    q = int(input())
    row = [i for i in range(1,n+1)]
    column = [i for i in range(1,n+1)]
    is_reverse = False
    for _ in range(q):
        query, *li = map(int, input().split())
        if query == 1:
            a = li[0]
            b = li[1]
            row[a-1],row[b-1] = row[b-1],row[a-1],
        elif query == 2:
            a = li[0]
            b = li[1]
            column[a-1],column[b-1] = column[b-1], column[a-1],
        elif query == 3:
            row,column, = column, row
            is_reverse = not is_reverse
        else:
            a = li[0]
            b = li[1]
            a -= 1
            b -= 1
            if not is_reverse:
                print(n * (row[a] - 1) + column[b] - 1)
            else:
                print(n * (column[b] - 1) + row[a] - 1)

if __name__ == '__main__':
    main()

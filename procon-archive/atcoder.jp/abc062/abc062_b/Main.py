if __name__ == '__main__':
    h,w = map(int,input().split())
    header = "#" * (w+2)
    l = []
    for i in range(h):
        row = "#"
        row += input()
        row += "#"
        l.append(row)

    print(header)
    for i in l:
        print(i)
    print(header)
def main():
    n,k = map(int, input().split())
    dic = {}
    for _ in range(n):
        a,b = map(int,input().split())
        if dic.get(a) is None:
            dic[a] = b
        else:
            dic[a] += b
    values = list(dic.keys())
    values.sort()
    for value in values:
        k -= dic[value]
        if k <= 0:
            print(value)
            exit()


if __name__ == '__main__':
    main()
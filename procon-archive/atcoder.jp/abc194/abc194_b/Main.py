def main():
    n = int(input())
    solo = float('inf')
    a_list = []
    b_list = []
    for i in range(n):
        a,b = map(int, input().split())
        a_list.append((a, i))
        b_list.append((b, i))
        solo = min(solo, a+b)
    a_list.sort()
    b_list.sort()
    ans = float('inf')
    if a_list[0][1] == b_list[0][1]:
        ans = min(max(a_list[0][0],b_list[1][0]), max(a_list[1][0],b_list[0][0]))
    else:
        ans = max(a_list[0][0],b_list[0][0])
    ans = min(ans, solo)
    print(ans)


if __name__ == '__main__':
    main()

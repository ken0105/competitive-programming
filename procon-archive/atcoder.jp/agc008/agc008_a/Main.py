def main():
    x,y = map(int,input().split())
    ans = float('inf')
    if x < y:
        ans = min(ans, y- x)
    if -x <= y:
        ans = min(ans, 1 + y + x)
    if -y >= x:
        ans = min(ans, 1 -y -x)
    if -y >= -x:
        ans = min(ans, 2 + -y + x)
    print(ans)

if __name__ == '__main__':
    main()
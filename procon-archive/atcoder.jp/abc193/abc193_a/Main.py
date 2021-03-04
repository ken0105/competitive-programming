def main():
    a,b = map(int,input().split())
    ans = 100 - (b / a) * 100
    print(ans)

if __name__ == '__main__':
    main()


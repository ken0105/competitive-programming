def main():
    m,h = map(int, input().split())
    if h % m == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

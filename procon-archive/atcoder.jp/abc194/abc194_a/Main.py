def main():
    a,b = map(int, input().split())
    solid = a + b
    fat = b
    if solid >= 15 and fat >= 8:
        print(1)
    elif solid >= 10 and fat >= 3:
        print(2)
    elif solid >= 3:
        print(3)
    else:
        print(4)


if __name__ == '__main__':
    main()

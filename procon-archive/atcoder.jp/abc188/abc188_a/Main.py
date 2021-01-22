if __name__ == "__main__":
    a,b = map(int,input().split())
    if a > b:
        if b+3 > a:
            print("Yes")
        else:
            print("No")
    else:
        if a+3>b:
            print("Yes")
        else:
            print("No")
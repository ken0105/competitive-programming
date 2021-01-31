if __name__ == '__main__':
    a,b,c = map(int,input().split())
    if c == 0:
        if a == b:
            print("Aoki")
        elif a > b:
            print("Takahashi")
        else:
            print("Aoki")
    else:
        if a == b:
            print("Takahashi")
        elif a > b:
            print("Takahashi")
        else:
            print("Aoki")
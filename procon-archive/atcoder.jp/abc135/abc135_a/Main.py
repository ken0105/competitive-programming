if __name__ == "__main__":
    a,b = map(int,input().split())
    if abs(a+b)%2 == 1:
        print("IMPOSSIBLE")
    else:
        print((a+b)//2)
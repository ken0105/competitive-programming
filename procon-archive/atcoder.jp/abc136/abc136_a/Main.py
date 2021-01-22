if __name__ == "__main__":
    a,b,c = map(int,input().split())
    r = abs(a-b)
    print(max(0,c-r))
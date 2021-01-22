if __name__ == "__main__":
    n,m = map(int,input().split())
    print(pow(10,n,m**2)//m)
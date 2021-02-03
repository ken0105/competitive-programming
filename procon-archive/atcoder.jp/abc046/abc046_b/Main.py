if __name__ == '__main__':
    n,k = map(int,input().split())
    print(k * ((k-1)**(n-1)))
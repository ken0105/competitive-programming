if __name__ == '__main__':
    r,D,x, = map(int,input().split())
    ans = x
    for i in range(10):
        ans = ans * r - D
        print(ans)

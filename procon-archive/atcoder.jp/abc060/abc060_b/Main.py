if __name__ == '__main__':
    A,B,C = map(int,input().split())
    a = A
    for _ in range(10000):
        if a % B == C:
            print("YES")
            exit()
        a += A
    print("NO")
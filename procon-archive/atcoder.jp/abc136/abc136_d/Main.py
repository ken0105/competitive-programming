if __name__ == "__main__":
    s = input()
    n = len(s)
    child = [0] * n

    stock = 0
    for i in range(n):
        if s[i] == "R":
            stock += 1
        if s[i] == "L":
            child[i] += stock // 2
            child[i-1] += (stock+1) // 2
            stock = 0
    stock = 0
    for i in range(n-1,-1,-1):
        if s[i] == "L":
            stock += 1
        if s[i] == "R":
            child[i] += stock //2
            child[i+1] += (stock+1) //2
            stock = 0
    print(*child)



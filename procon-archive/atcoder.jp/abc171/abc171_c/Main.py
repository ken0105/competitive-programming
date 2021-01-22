if __name__ == "__main__":
    n = int(input())
    s = ""
    while n:
        s = chr(ord("a") + (n -1) % 26) + s
        n -= 1
        n //= 26
    print(s)
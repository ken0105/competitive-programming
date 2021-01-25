if __name__ == '__main__':
    n = int(input())
    l = [2,1]
    while len(l) < n + 1:
        l.append(l[-1] + l[-2])
    print(l[-1])
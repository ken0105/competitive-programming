if __name__ == '__main__':
    s = list(input())
    t = list(input())
    s.sort()
    t.sort(reverse=True)
    if s < t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    s = int(input())
    seen = set()

    seen.add(s)
    for i in range(2,1000100):
        if s % 2 == 0:
            s //= 2
        else:
            s = 3 * s + 1

        if s in seen:
            print(i)
            exit()
        seen.add(s)





if __name__ == "__main__":
    n = int(input())
    i = 1
    li = []
    while i ** 2 <= n:
        if i ** 2 == n:
            li.append(i)
            break

        if n % i == 0:
            li.append(n//i)
            li.append(i)

        i += 1

    li.sort()
    for i in range(len(li)):
        print(li[i])

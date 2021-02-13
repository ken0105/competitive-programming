def main():
    x = int(input())
    time = 0
    total = 0
    while True:
        time += 1
        total += time
        if total >= x:
            print(time)
            exit()

if __name__ == '__main__':
    main()

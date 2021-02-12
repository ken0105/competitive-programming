def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    while h != [0] * n:
        for index, num in enumerate(h):
            if num == 0:
                continue
            else:
                cnt += 1
                new_h = h[index:]
                for index2, num2, in enumerate(new_h):
                    if num2 == 0:
                        break
                    else:
                        h[index2 + index] -= 1
                break
    print(cnt)


if __name__ == '__main__':
    main()

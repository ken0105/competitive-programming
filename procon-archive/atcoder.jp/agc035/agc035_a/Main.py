from collections import Counter


def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt_a = Counter(a)
    if len(list(cnt_a.keys())) == 1:
        if a[0] == 0:
            print("Yes")
        else:
            print("No")
        exit()
    if len(list(cnt_a.keys())) == 2:
        if cnt_a.get(0) and cnt_a.get(0) * 3 == n:
            print("Yes")
        else:
            print("No")
        exit()
    if len(list(cnt_a.keys())) == 3:
        if all([i == n // 3 for i in list(cnt_a.values())]):
            keys = list(cnt_a.keys())
            if keys[0] ^ keys[1] == keys[2]:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")













if __name__ == '__main__':
    main()


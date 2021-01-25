from collections import Counter

if __name__ == '__main__':
    w = input()
    cnt_w = Counter(w)
    for i in cnt_w.values():
        if i % 2 == 1:
            print("No")
            exit()
    print("Yes")
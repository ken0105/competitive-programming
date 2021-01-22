from collections import Counter

if __name__ == '__main__':
    s = input()
    s_cnt = Counter(s)
    value = s_cnt.values()
    for i in value:
        if i != 2:
            print("No")
            exit()
    print("Yes")

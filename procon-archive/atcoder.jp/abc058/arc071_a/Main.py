from collections import Counter

def main():
    n = int(input())
    s = input()
    s_cnt = Counter(s)
    for _ in range(n-1):
        string = input()
        string_cnt = Counter(string)
        for i in list(s_cnt.keys()):
            if string_cnt.get(i) is None:
                s_cnt.pop(i)
            else:
                s_cnt[i] = min(s_cnt[i], string_cnt.get(i))
    ans = []
    for c,i in list(s_cnt.items()):
        for _ in range(i):
            ans.append(c)
    ans.sort()
    print("".join(ans))



if __name__ == '__main__':
    main()

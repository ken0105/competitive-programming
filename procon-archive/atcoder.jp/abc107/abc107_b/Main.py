if __name__ == '__main__':
    h,w = map(int,input().split())
    p_throwable = set()
    for i in range(w):
        p_throwable.add(i)
    ans = []
    for _ in range(h):
        a = input()
        if "#" not in a:
            continue
        ans.append(a)
        p_throwable_tmp = set()
        for index, p, in enumerate(a):
            if p == ".":
                p_throwable_tmp.add(index)
        p_throwable = p_throwable.intersection(p_throwable_tmp)

    li = []
    for i in ans:
        li_tmp = ""
        for index,j in enumerate(i):
            if index in p_throwable:
                continue
            li_tmp += j
        li.append(li_tmp)

    for i in li:
        print(i)

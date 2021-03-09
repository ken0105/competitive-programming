def main():
    n,m,q, = map(int, input().split())
    adj_li = [[] for i in range(n+1)]

    for i in range(m):
        u,v = map(int, input().split())
        adj_li[u].append(v)
        adj_li[v].append(u)
    c = [0] + list(map(int, input().split()))
    for i in range(q):
        command, *li = map(int, input().split())
        if command == 1:
            print(color(c, li[0]))
            rewrite(c, adj_li, li[0])
        else:
            print(color(c, li[0]))
            c[li[0]] = li[1]

def color(c, index):
    return c[index]

def rewrite(c, adj_li, index):
    base_color = c[index]
    for i in adj_li[index]:
        c[i] = base_color

if __name__ == '__main__':
    main()

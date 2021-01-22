from itertools import permutations

if __name__ == '__main__':
    n = int(input())
    store = int(input())
    order = int(input())
    stores = [0, n]
    for _ in range(store - 1):
        stores.append(int(input()))
    stores.sort()
    orders = []
    for _ in range(order):
        orders.append(int(input()))


    def _bin_search(stores, num):
        s = 0
        e = len(stores) - 1
        while s + 1 < e:
            mid = (s + e) // 2
            if num > stores[mid]:
                s = mid
            elif num < stores[mid]:
                e = mid
            else:
                return 0
        r = min(abs(num - stores[s]), abs(num - stores[e]))
        return r


    ans = 0
    for o in orders:
        ans += _bin_search(stores, o)
    print(ans)

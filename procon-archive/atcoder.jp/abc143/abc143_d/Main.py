from bisect import bisect, bisect_right, bisect_left

if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            target = l[j+1:]
            max_c = l[i] + l[j] - 1
            min_c = abs(l[i] - l[j]) + 1
            min_c_index = bisect_left(target,min_c)
            max_c_index = bisect_right(target,max_c)
            ans += (max_c_index - min_c_index)
    print(ans)
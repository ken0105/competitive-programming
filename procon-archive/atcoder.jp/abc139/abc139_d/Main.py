from bisect import bisect, bisect_right, bisect_left

if __name__ == "__main__":
    n = int(input())
    print((1+n-1)* (n -1) //2)

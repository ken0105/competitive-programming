from itertools import accumulate

if __name__ == '__main__':
    h = int(input())
    div = 0
    while h > 1:
        h = h //2
        div += 1
    ans = 0
    for i in range(0,div):
        ans = ans + 2 ** i
    print(ans+2**div)
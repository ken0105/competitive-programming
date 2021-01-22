import math

if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a_max = max(a)
    a_second = 0
    a_max_count = 0
    for i in a:
        if i == a_max:
            a_max_count += 1
        else:
            a_second = max(a_second,i)
    for i in a:
        if i == a_max and a_max_count <= 1:
            print(a_second)
        elif i == a_max and a_max_count > 1:
            print(a_max)
        else:
            print(a_max)
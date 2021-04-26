import itertools


def main():
    l = []
    for _ in range(5):
        l.append(int(input()))
    k = int(input())
    for i,j in itertools.combinations(l,2):
        if abs(i-j) > k:
            print(":(")
            exit()
    print("Yay!")


if __name__ == '__main__':
    main()

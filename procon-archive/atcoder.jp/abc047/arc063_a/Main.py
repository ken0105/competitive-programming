def main():
    s = input()
    add = [s[0]]
    for i,color in enumerate(s):
        if color == add[-1]:
            continue
        else:
            add.append(color)
    print(len(add) - 1)

if __name__ == '__main__':
    main()

if __name__ == '__main__':
    s = input()
    ideal1 = 0
    ideal2 = 0
    for i, color in enumerate(s):
        if i % 2 == 1 and color == "1":
            ideal1 += 1
        if i % 2 == 0 and color == "0":
            ideal1 += 1

    for i, color in enumerate(s):
        if i % 2 == 1 and color == "0":
            ideal2 += 1
        if i % 2 == 0 and color == "1":
            ideal2 += 1
    print(min(ideal1,ideal2))

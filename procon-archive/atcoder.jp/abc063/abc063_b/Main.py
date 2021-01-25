if __name__ == '__main__':
    s = input()
    set_s = set(s)
    if len(s) == len(set_s):
        print("yes")
    else:
        print("no")

import re

if __name__ == '__main__':
    s = input()
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    s = set(s)
    for i in s:
        if i in alphabet:
            alphabet.remove(i)
    if len(alphabet) == 0:
        print("None")
    else:
        print(alphabet[0])
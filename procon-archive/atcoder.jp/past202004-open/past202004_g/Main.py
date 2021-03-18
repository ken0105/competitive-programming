from collections import deque
from string import ascii_lowercase


def main():
    q = int(input())
    strings = deque()
    for _ in range(q):
        query, *li = input().split()
        if query == "1":
            char = li[0]
            number = int(li[1])
            strings.append((char, number))
        else:
            deletion = int(li[0])
            d = {}
            for i in ascii_lowercase:
                d[i] = 0
            while strings:
                char, number, = strings.popleft()
                if number >= deletion:
                    number -= deletion
                    d[char] += deletion
                    strings.appendleft((char, number))
                    break
                else:
                    deletion -= number
                    d[char] += number
            ans = 0
            for i in ascii_lowercase:
                if i in d.keys():
                    ans += (d[i] ** 2)
            print(ans)




if __name__ == '__main__':
    main()
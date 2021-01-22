from itertools import accumulate


def best_choice(hand):
    if hand == "r":
        return p
    if hand == "s":
        return r
    if hand == "p":
        return s


if __name__ == '__main__':
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    best = [""] * n
    for i in range(len(t)):
        if t[i] == "r":
            best[i] = "p"
        elif t[i] == "s":
            best[i] = "r"
        else:
            best[i] = "s"
    score = 0
    for i in range(len(t)):
        if i == 0:
            score += best_choice(t[i])
            continue
        if i - k >= 0 and best[i] == best[i-k]:
            best[i] = ""
            continue
        else:
            score += best_choice(t[i])
    print(score)

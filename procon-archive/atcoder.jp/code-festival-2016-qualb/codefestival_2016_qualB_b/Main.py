if __name__ == '__main__':
    n,a,b = map(int,input().split())
    s = input()
    passed = 0
    f_passed = 0
    player = []
    for i in s:
        if i == "c":
            player.append("No")
            continue
        elif i == "a":
            if passed < a:
                passed += 1
                player.append("Yes")
                continue
            elif passed < a + b:
                passed += 1
                player.append("Yes")
                continue
        else:
            if passed < a + b and f_passed < b:
                passed += 1
                f_passed += 1
                player.append("Yes")
                continue
        player.append("No")
    for p in player:
        print(p)

from itertools import permutations


def main():
    S = [input() for _ in range(3)]
    letters = set("".join(S))
    if len(letters) > 10:
        print("UNSOLVABLE")
        exit()

    letters = list(letters)
    idx = {c : i for i,c in enumerate(letters)}
    for perm in permutations(range(10)):
        nums = []
        for s in S:
            n = 0
            if perm[idx[s[0]]] == 0:
                break
            for c in s:
                n = n * 10 + perm[idx[c]]
            nums.append(n)
        if len(nums) == 3 and nums[0] + nums[1] == nums[2]:
            print(*nums, sep="\n")
            exit()
    print("UNSOLVABLE")



if __name__ == '__main__':
    main()

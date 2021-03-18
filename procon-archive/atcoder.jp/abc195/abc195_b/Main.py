import math


def main():
    a,b,w = map(int, input().split())
    w *= 1000
    # answers = []
    # for x in range(0,1001):
    #     for y in range(0,1001):
    #         if x * a + y * b > w:
    #             answers.append(x + y)
    #
    # if len(answers) == 0:
    #     print("UNSATISFIABLE")
    # else:
    #     answers.sort()
    #     print(answers[0],answers[-1])

    min_candidate = math.ceil(w / b)
    max_candidate = math.floor(w / a)
    if max_candidate < min_candidate:
        print("UNSATISFIABLE")
    else:
        print(min_candidate, max_candidate)

if __name__ == '__main__':
    main()

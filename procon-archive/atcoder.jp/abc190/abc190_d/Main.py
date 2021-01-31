if __name__ == '__main__':
    n = int(input())
    def make_divisors(x):
        cnt = 0
        for i in range(1, int(x**0.5)+1):
            if x % i == 0 and (i % 2 == 1 or x // i % 2 == 1):
                if i ** 2 == x:
                    cnt += 1
                else:
                    cnt += 2
                # if i != n // i:
                #     cnt += 1

        # divisors.sort()
        return cnt

    print(make_divisors(n * 2))
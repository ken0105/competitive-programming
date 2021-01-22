import math

if __name__ == '__main__':
    a,b,c,d = map(int,input().split())
    lcm = c * d // math.gcd(c, d)
    can_b_div_c = b // c
    can_b_div_d = b // d
    can_b_div_lcm = b // lcm
    a -= 1
    can_a_div_c = a // c
    can_a_div_d = a // d
    can_a_div_lcm = a // lcm

    ans = (b - (can_b_div_c + can_b_div_d - can_b_div_lcm)) - (a - (can_a_div_c + can_a_div_d - can_a_div_lcm))
    print(ans)


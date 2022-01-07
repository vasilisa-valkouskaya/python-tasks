import math


def main():
    print('y =', count_func(24, 2, 32))


def count_func(a, b, c):
    x1 = (b + math.sqrt(abs(pow(b, 2) - 4*a*c))) / (2*a)
    x2 = (b - math.sqrt(abs(pow(b, 2) - 4*a*c))) / (2*a)
    y = (pow(math.e, -x1) + pow(math.e, -x2)) / 2
    return y


main()

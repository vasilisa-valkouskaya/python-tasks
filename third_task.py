import math


def main():
    number = int(input('enter the number: '))
    print(calc_value(number))


def calc_value(n):
    num = 1
    result = math.sin(1)

    for i in range(1, n):
        num += 1
        result += math.sin(num)
    return 1/result


main()

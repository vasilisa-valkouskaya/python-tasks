def main():
    value = int(input('Enter month number'))
    get_month(value)


def get_month(value):
    match value:
        case 1:
            print('February')
        case 2:
            print('March')
        case 3:
            print('April')
        case 4:
            print('May')
        case 5:
            print('June')
        case 6:
            print('July')
        case 7:
            print('August')
        case 8:
            print('September')
        case 9:
            print('October')
        case 10:
            print('November')
        case 11:
            print('December')
        case 12:
            print('January')
        case _:
            print('Month number is not correct')


main()

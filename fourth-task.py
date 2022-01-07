import statistics


def main():
    print(find_vector())


def find_vector():
    matrix = [[7, 2, 3, 4],
              [5, 6, 9, 8],
              [8, 14, 11, 23]]

    vector = []

    for i in range(0, len(matrix)):
        vector.append(statistics.mean(matrix[i]))
    return vector


main()

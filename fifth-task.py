import string


def main():
    print(change_letters())


def change_letters():
    text = "Hello, my friend. How are you?"
    text_list = text.translate(str.maketrans(dict.fromkeys(string.punctuation))).split()
    for i in range(0, len(text_list)):
        word = text_list[i]
        text_list[i] = word[-1] + word[0:-1]

    return ' '.join(text_list)


main()





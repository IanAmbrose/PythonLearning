import random
import string


def gen(size, list):

    for i in range(size):
        list.append(
            random.choice(
                string.ascii_uppercase
                + string.digits
                + string.ascii_lowercase
                + string.punctuation
            )
        )
        new = "".join(list)
    print(new)


if __name__ == "__main__":
    list = []
    size = int(input("length of the password to generate\n:"))
    gen(size, list)
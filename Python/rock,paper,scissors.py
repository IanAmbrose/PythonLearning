import random


def shoot():
    val = random.randrange(1, 4)
    return val


def type(inp):
    if inp == 1:
        ans = "rock"
    elif inp == 2:
        ans = "paper"
    elif inp == 3:
        ans = "Scissors"
    return ans


def display(result, ans1, ans2):
    print(f"You chose {ans1}")
    print(f"AI chose {ans2}")
    print(f"You {result}")


def compare(inp, val):
    compare = val - inp
    if compare == 0:
        result = "DRAW"
    elif compare == 2:
        result = "WIN"
    elif compare == 1:
        result = "LOSE"
    elif compare < 0:
        if val == 2:
            result = "WIN"
        elif val == 1 & inp == 2:
            result = "WIN"
        else:
            result = "LOSE"
    return result


if __name__ == "__main__":

    inp = int(
        input(
            """
    1. rock
    2. paper
    3. scissors
    """
        )
    )

    val = shoot()
    ans_1 = type(inp)
    ans_2 = type(val)
    result = compare(inp, val)
    display(result, ans_1, ans_2)

import sys


def guessed(letter):
    if letter not in guessed_letter:
        guessed_letter.append(letter)
        new = ",".join(guessed_letter)
        print(f"Letters Guessed = ({new[1::]})")
    else:
        print(f"Letter already Guessed")
    return guessed_letter


def health(lives, word):
    if lives > 0:
        print(f"Lives remaining - {lives}")
    else:
        print("Game over - no more lives")
        print(f"Word not guessed was - {word}")
        sys.exit()


def guess():
    letter = str(input("Enter a letter"))
    while True:
        if len(letter) > 1:
            print("Only guess a single letter")
            letter = str(input("Enter a letter"))
        else:
            break
    return letter


def main(word, display, lives, letter):
    while True:
        if display == word:
            print(f"\n\n --- HANGMAN --- \n Word - {display}\n")
            print(
                f"You Have guessed the word correctly - Congratulations \nWord Guessed - {word}"
            )
            break
        else:
            print(f"\n\n --- HANGMAN --- \n Word - {display}\n")
            guessed_letters = guessed(letter)
            health(lives, word)
            letter = guess()

        if letter not in word and letter not in guessed_letters:
            lives -= 1

        elif letter in word:
            count = 0
            for i in word:
                count += 1
                if i == letter:
                    display = display[0 : count - 1] + letter + display[count:]


if __name__ == "__main__":
    word = "invisible"
    guessed_letter = []
    display = len(word) * "_"
    lives = 9
    letter = ""

    main(word, display, lives, letter)
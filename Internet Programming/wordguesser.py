# Name: Wade Moulton
# Date: 09/25/2020
# Class: CS 4720
# Section: W01
# Instructor: Dr. Sarah North

# set the word once and then convert to list for easier iteration
word = 'FOX'
word_list = list(word)
final_word = []
guessed = []

def guessLetter(ltr):
    # convert letter to uppercase
    ltr = ltr.upper()

    # first check if the letter is in the word or not
    # if letter is in word, change all occurrences of blank letters in final_word to match at correct index
    # then check if the letter has been guessed, if not add to guessed array
    # give user feedback based on conditions
    if ltr in word_list or ltr.upper() in word_list:
        for i in range(len(word_list)):
            if word_list[i] == ltr or word_list[i].lower == ltr:
                final_word[i] = ltr
        if not (ltr in guessed or ltr.lower() in guessed):
            guessed.append(ltr)
            print(f"You found a new letter! {ltr} is in the word!")
            print(f"Your current progress: {''.join(str(x) for x in final_word)}")
        else:
            print(f"The letter {ltr} is in the word, but you already guessed it. Try again!")
            print(f"Here are your guessed letters: {','.join(str(x) for x in guessed)}")
            print(f"Your current progress: {''.join(str(x) for x in final_word)}")
    else:
        if not (ltr in guessed or ltr.lower() in guessed):
            guessed.append(ltr)
            print(f"The letter {ltr} is not in the word. Try again!")
        else:
            print(f"The letter {ltr} is not in the word and you have already guessed it. Try again!")
            print(f"Here are your guessed letters: {','.join(str(x) for x in guessed)}")


def main():
    print(f"I'm thinking of a {len(word)} letter word! Let's see if you can guess it!")
    for i in range(len(word_list)):
        final_word.append('_')
    while word_list != final_word:
        ltr = input('Enter a letter to guess: ').lower()
        # check if input is alphabetic
        if ltr.isalpha():
            guessLetter(ltr)
        else:
            print('Input must be a letter. Try again!')

    print("You found the word! Congratulations you win!")


if __name__ == '__main__':
    main()

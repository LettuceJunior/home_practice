# Problem Set 2, hangman.py
# Name: Anna Latuil
# Collaborators: Max Havriluk
# Time spent: 3 nights

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word = set(secret_word)
    letters_guessed = set(letters_guessed)
    if secret_word.issubset(letters_guessed):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed, new_lttr):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letters_guessed.append(new_lttr)
    res = ''
    for lttr in secret_word:
        if lttr in letters_guessed:
            res = res + lttr
        else:
            res = res + '_ '
    print (res)
    return (res)
    



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = string.ascii_lowercase
    for lttr in letters_guessed:
        available_letters = available_letters.replace(lttr, '')
    return available_letters 


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''

    guesses = 6
    warnings = 3
    #secret_word = 'text'
    letters_guessed = []
    res = ''
    print ("Nice to see you here! It's time to play :)")
    print ("My word contains", len(secret_word), "letters. Try to guess)")
    a=("-"*30)
    print (a)
    print ("You have", guesses, "attempts and", warnings, "warnings")
    print (string.ascii_lowercase)

    while guesses > 0:
        new_lttr = input('Guess:').lower()

        if not str.isalpha(new_lttr):
            print('Warning! It must be a letter!')
            if warnings > 0:
                warnings = warnings - 1
            elif warnings == 0:
                guesses = guesses - 1
            get_guessed_word(secret_word, letters_guessed, new_lttr)

        elif not len(new_lttr) == 1:
            print('Warning! You can try only one letter at time')
            if warnings > 0:
                warnings = warnings - 1
            elif warnings == 0:
                guesses = guesses - 1
            get_guessed_word(secret_word, letters_guessed, new_lttr)

        elif new_lttr in letters_guessed:
            print('You have already tried this letter!')
            if warnings>0:
              warnings=warnings-1
            elif warnings==0:
              guesses=guesses-1
            get_guessed_word(secret_word, letters_guessed, new_lttr)

        else:
            if new_lttr in secret_word:
              print('Nice try!')
            else:
              if new_lttr == "a":
                guesses = guesses - 2
              elif new_lttr == "e":
                guesses = guesses - 2
              elif new_lttr == "i":
                guesses = guesses - 2
              elif new_lttr == "o":
                guesses = guesses - 2
              elif new_lttr == "u":
                guesses = guesses - 2
              else: 
                guesses = guesses - 1
              print('Oops! That letter is not in my word')
            get_guessed_word(secret_word, letters_guessed, new_lttr)

        if guesses == 0:
            print('Sorry, you ran out of guesses. The word was', secret_word)
            break

        if is_word_guessed(secret_word, letters_guessed) == True:
            print('Congratulations, you won!')
            break

        print (a)
        print ("You have", guesses, "attempts and", warnings, "warnings")
        print (get_available_letters(new_lttr))




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_word = my_word.replace(' ', '')
    my_word_lttr = set(my_word)
    if len(my_word) == len(other_word): 
      for i,l in enumerate(my_word):
        if l == "_":
          if other_word[i] in my_word_lttr:
            return False
        else:
          if l != other_word[i]:
            return False
    else:
      return False
    return True
        
      



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    box = []
    for w in wordlist:
        if match_with_gaps(my_word, w):
          box.append(w)

    if len(box) > 0:
      print(box)
    else:
      print("No matches found")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 6
    warnings = 3
    #secret_word = 'text'
    letters_guessed = []
    print ("Nice to see you here! It's time to play :)")
    print ("My word contains", len(secret_word), "letters. Try to guess)")
    a=("-"*30)
    print (a)
    print ("You have", guesses, "attempts and", warnings, "warnings")
    print (string.ascii_lowercase)

    while guesses > 0:
        new_lttr = input('Guess:').lower()

        if not str.isalpha(new_lttr):

          if new_lttr == "*":
            my_word = get_guessed_word(secret_word, letters_guessed, new_lttr)
            print ("Possible matches:")
            show_possible_matches(my_word)

          else:
            print('Warning! It must be a letter!')

            if warnings > 0:
                warnings = warnings - 1

            elif warnings == 0:
                guesses = guesses - 1

        elif not len(new_lttr) == 1:
            print('Warning! You can try only one letter at time')

            if warnings > 0:
                warnings = warnings - 1

            elif warnings == 0:
                guesses = guesses - 1

            get_guessed_word(secret_word, letters_guessed, new_lttr)

        elif new_lttr in letters_guessed:
            print('You have already tried this letter!')

            if warnings>0:
              warnings=warnings-1

            elif warnings==0:
              guesses=guesses-1
              
            get_guessed_word(secret_word, letters_guessed, new_lttr)

        else:
            if new_lttr in secret_word:
              print('Nice try!')
            else:
              if new_lttr == "a":
                guesses = guesses - 2

              elif new_lttr == "e":
                guesses = guesses - 2

              elif new_lttr == "i":
                guesses = guesses - 2
                
              elif new_lttr == "o":
                guesses = guesses - 2

              elif new_lttr == "u":
                guesses = guesses - 2

              else: 
                guesses = guesses - 1
  
              print('Oops! That letter is not in my word')

            get_guessed_word(secret_word, letters_guessed, new_lttr)

        if guesses == 0:
            print('Sorry, you ran out of guesses. The word was', secret_word)
            break

        if is_word_guessed(secret_word, letters_guessed) == True:
            print('Congratulations, you won!')
            print("Your total score:", guesses*len(set(secret_word)))
            break

        print (a)
        print ("You have", guesses, "attempts and", warnings, "warnings")
        print (get_available_letters(new_lttr))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

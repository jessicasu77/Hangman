import random
import string

WORDLIST_FILENAME = "words.txt"
guesses = 6
letters_guessed = []
warnings = 3 
vowels = ["a", "e", "i", "o", "u"]

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


def get_guessed_word(secret_word, letters_guessed):
    guess = []
    for char in secret_word:
      if char in letters_guessed:
        guess.append(char + " ")
      else:
        guess.append("_ ")
    return ''.join(guess)


def is_word_guessed(secret_word, letters_guessed, i):
    for char in secret_word:
      if char in letters_guessed:
        i += 1
    if i == len(secret_word):
      return True
    else:
      return False


def get_available_letters(letters_guessed):
    letters_available = []
    for char in string.ascii_lowercase:
      if char not in letters_guessed:
        letters_available.append(char)
    return ''.join(letters_available)


def is_input_valid(letter):
    if letter.isalpha() == True:
      return True
    else:
      return False


def match_with_gaps(my_word, other_word):
    is_it_a_match = []
    my_word = my_word.replace(" ", "")
    if len(my_word) == len(other_word):
      i = 0
      for i in range (len(my_word)):
        my_char = my_word[i]
        other_char = other_word[i]
        if my_word[i] in string.ascii_lowercase:
          if my_char == other_char:
            is_it_a_match.append(True)
          else:
            return False
    else: 
      return False
    if False not in is_it_a_match:
        return True
          

def show_possible_matches(my_word):
    possible_matches = []
    for i in wordlist:
      if match_with_gaps(my_word, i) == True:
        possible_matches.append(i)
    if len(possible_matches) > 0:
      print(', '.join(possible_matches))
    else:
      print("No matches found.")


def calculate_score(guesses, secret_word):
    unique_letters = []
    for char in secret_word:
        if char not in unique_letters:
            unique_letters.append(char)
    score = len(unique_letters * guesses)
    return score
    
def hangman(secret_word):
    global guesses
    global letters_guessed
    global warnings
    global vowels
    if guesses == 6:
      length = len(secret_word)
      print("Welcome to the game Hangman!\nI am thinking of a word that is", length, "letters long.")
    while guesses > 0 and is_word_guessed(secret_word, letters_guessed, 0) == False: 
      available_letters = get_available_letters(letters_guessed)  
      print("---------------------------------------------------------------------------\nYou have", guesses, "guesses left.\nHere are your available letters:", available_letters)   
      letter = input("Pick a letter: ")
#check if input is a letter
      if is_input_valid(letter) == True:
          letter = letter.lower()
#check if letter was already guessed (if it was, exits)
          if letter in letters_guessed:
            if warnings > 0:
              warnings -=1
              print("Oops. You've already guessed that letter. You've lost a warning. Warnings left:", warnings)
            else:
              guesses -=1
              print("Oops. You've already guessed that letter. You have no more warnings and now have lost a guess. Guesses:", guesses)
          else:    
#add letter to letters_guessed list if letter wasn't guessed already
            letters_guessed.append(letter)
#determine if letter is in secret word
            if letter in secret_word:
              print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
#loses guesses for wrong guess
            else:
              if letter in vowels:
                guesses -=2
              else:
                guesses -=1
              print("Oops! That letter is not in the secret word!: ", get_guessed_word(secret_word, letters_guessed))
#if input is not a letter **is there a way to put this closer to the input part of code
      else:
        if warnings <= 0:
          guesses -=1
          print("Oops! Only letters are valid guesses. Since you have no warnings left, you lost 1 guess.")
        else:
          warnings -=1
          print("Oops! Only letters are valid guesses. You have", warnings, "warnings left.")
      if is_word_guessed(secret_word, letters_guessed, 0) == True:
          print("Congratulations! You won! The word was", secret_word + "!\nYour score is", calculate_score(guesses, secret_word))
      else:
        if guesses == 0:  
          print("Sorry! You lost the game, because you ran out of guesses. The word was", secret_word)
        else:      
          hangman(secret_word)


def hangman_with_hints(secret_word):
    global guesses
    global letters_guessed
    global warnings
    global vowels
    if guesses == 6:
      length = len(secret_word)
      print("Welcome to the game Hangman with hints!\nI am thinking of a word that is", length, "letters long.")
    while guesses > 0 and is_word_guessed(secret_word, letters_guessed, 0) == False: 
      available_letters = get_available_letters(letters_guessed)  
      print("--------------------------------------------------------------------------\nYou have", guesses, "guesses left.\nHere are your available letters:", available_letters)   
      user_input = input("Pick a letter (or * to print out words that match the guess): ")
#give user a hint
      if user_input == "*":
          my_word = get_guessed_word(secret_word, letters_guessed)
          print("Here are words that could be the possible secret word: ")
          show_possible_matches(my_word)      
#check if input is a letter
      else:
        if is_input_valid(user_input) == True:
            user_input = user_input.lower()
#check if letter was already guessed (if it was, exits)
            if user_input in letters_guessed:
              if warnings > 0:
                warnings -=1
                print("Oops. You've already guessed that letter. You've lost a warning. Warnings left:", warnings)
              else:
                guesses -=1
                print("Oops. You've already guessed that letter. You have no more warnings and now have lost a guess. Guesses:", guesses)
            else:    
#add letter to letters_guessed list if letter wasn't guessed already
              letters_guessed.append(user_input)
#determine if letter is in secret word
              if user_input in secret_word: print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
#loses guesses for wrong guess
              else:
                if user_input in vowels:
                  guesses -=2
                else:
                  guesses -=1
                print("Oops! That letter is not in the secret word!: ", get_guessed_word(secret_word, letters_guessed))
#lose warning if input is not a letter **is there a way to put this closer to the input part of code
        else:
          if warnings <= 0:
            guesses -=1
            print("Oops! Only letters are valid guesses. Since you have no warnings left, you lost 1 guess.")
          else:
            warnings -=1
            print("Oops! Only letters are valid guesses. You have", warnings, "warnings left.")       
      if is_word_guessed(secret_word, letters_guessed, 0) == True:
          print("Congratulations! You won! The word was", secret_word + "!\nYour score is", calculate_score(guesses, secret_word))
      else:
        if guesses == 0:  
          print("Sorry! You lost the game, because you ran out of guesses. The word was", secret_word)
        else:      
          hangman_with_hints(secret_word)


game_picked = input("Welcome to the game Hangman!\nHere's how it works: The computer selects a random word and you must guess the secret word!\nHere are the rules:\n1. There are two versions of the game: One with hints and one without hints. (A hint would show all possible matches to the secret word based on the letters already guessed.)\n2. All users start with 6 guesses and 3 warnings.\n3. Please guess a lowercase or uppercase letter. If the user inputs anything besides a letter (unless inputting \"*\" for requesting a hint in the hint version), the user loses one warning.\n4. If the user inputs a letter that has already been guessed, the user loses one warning.\n5. If no warnings are left, the user loses a guess.\n6. If the user inputs a letter that hasn't been guessed before and in the secret word, the user loses no guesses.\n7. If the user inputs a consonant that hasn't been guessed and not in the secret word, the user loses one guess.\n8. If the user inputs a vowel that hasn't been guessed and not in the secret word, the user loses two guesses (Vowels are a, e, i, o, u.)\n9. Game ends if the user runs out of guesses or constructs the full word.\n10. You win if you have guessed the secret word before running out of guesses.\n11. If you win, your score will be calculated by the number of guesses remaining times the number of unique letters in the secret word.\nType \"hints\" to play hangman with hints and \"hangman\" to play hangman without hints: ")
wordlist = load_words()  
secret_word = choose_word(wordlist)
print(secret_word)
if game_picked == "hints":
  hangman_with_hints(secret_word)
if game_picked == "hangman":
  hangman(secret_word)

###### Hangman

How it works: The computer selects a random word and the user must guess the secret word!

The rules:
1. There are two versions of the game: One with hints and one without hints. (A hint would show all possible matches to the secret word based on the letters already guessed.)
2. All users start with 6 guesses and 3 warnings.
3. Please guess a lowercase or uppercase letter. If the user inputs anything besides a letter (unless inputting "*" for requesting a hint in the hint version), the user loses one warning.
4. If the user inputs a letter that has already been guessed, the user loses one warning.
5. If no warnings are left, the user loses a guess.
6. If the user inputs a letter that hasn't been guessed before and in the secret word, the user loses no guesses.
7. If the user inputs a consonant that hasn't been guessed and not in the secret word, the user loses one guess.
8. If the user inputs a vowel that hasn't been guessed and not in the secret word, the user loses two guesses (Vowels are a, e, i, o, u.)
9. Game ends if the user runs out of guesses or constructs the full word.
10. You win if you have guessed the secret word before running out of guesses.
11. If you win, your score will be calculated by the number of guesses remaining times the number of unique letters in the secret word.



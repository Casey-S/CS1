import hangman
import pytest

'''
def isWordGuessed(secretWord, correctGuesses):

    secretWord: string, the random word the user is trying to guess.
    This is selected on line 9.
    correctGuesses: list of letters that have been guessed correctly so far.
    returns: boolean, True if all letters of secretWord are in correctGuesses;
    False otherwise

    if correctGuesses in secretWord:
        return True
    else:
        return False


def testisWordGuessed():
    x = isWordGuessed('cat', ['c', 't', 'a'])
    assert x is True
    x = isWordGuessed('cat', [])
    assert x is False
'''


def test_getGuessedLetter(secretWord, correctGuesses):
    '''
    secretWord: string, the random word the user is trying to guess.
    This is selected on line 9.
    correctGuesses: list of letters that have been guessed correctly so far.
    returns: string, of letters and underscores. For letters in the word that
    the user has guessed correctly,
    the string should contain the letter at the correct position.
    For letters in the word that the user has not yet guessed,
    shown an _ (underscore) instead.
    '''

    output = ['_'] * len(secretWord)
    while True:
        userGuess = raw_input("Guess a letter: ")
        if userGuess in secretWord:
            print("%s is correct." % userGuess)
            for i, letter in enumerate(secretWord):
                if userGuess is letter:
                    output[i] = letter
        else:
            print("Incorrect, try again.")
        correctGuesses = ''.join([x + "" for x in output])
        print(correctGuesses)
        

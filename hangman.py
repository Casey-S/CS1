import random


def loadWord():
    '''
    Opens words.txt file as variable f.
    Saves read lines to variable wordsList, then removes spaces from words.
    Chooses a random word from wordsList and saves it as variable secretWord,
    then returns it.
    '''
    f = open('words.txt', 'r')
    wordsList = f.readlines()
    f.close()

    wordsList = wordsList[0].split(' ')
    secretWord = random.choice(wordsList)
    return secretWord


def isWordGuessed(secretWord, correctGuesses):
    '''
    secretWord: string, the random word the user is trying to guess.
    This is selected on line 9.
    correctGuesses: list of letters that have been guessed correctly so far.
    returns: boolean, True if all letters of secretWord are in correctGuesses;
    False otherwise
    '''
    if correctGuesses in secretWord:
        return True
    else:
        return False


def getGuessedLetter(secretWord):
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
    letterArray = ['_'] * len(secretWord)
    numberOfGuesses = 7
    while numberOfGuesses > 1:
        numberOfGuesses = numberOfGuesses - 1
        print("You have %s guesses left" % numberOfGuesses)
        userGuess = raw_input("Guess a letter: ")
        if userGuess in secretWord:
            print("%s is correct." % userGuess)
            for i, letter in enumerate(secretWord):
                if userGuess is letter:
                    letterArray[i] = letter
        else:
            print("Incorrect, try again.")
        correctGuesses = ''.join([x + "" for x in letterArray])
        print(correctGuesses)
        if correctGuesses in secretWord:
            break
            return correctGuesses


def getAvailableLetters(correctGuesses):
    '''
    correctGuesses: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up a game of Hangman in the command line.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to guess one letter per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    print("The word has %s letters" % len(secretWord))
    getGuessedLetter(secretWord)


secretWord = loadWord()
hangman(loadWord())

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


def getGuessedLetter(secretWord, letterArray, incorrectArray):
    '''
    secretWord: string, the random word the user is trying to guess.
    letterArray: array of underscores the length of secretWord.
    incorrectArray: array of incorrect guessed letters.
    For letters in the word that the user has not yet guessed,
    shown an _ (underscore) instead.
    '''
    userGuess = raw_input("Guess a letter: ")
    if userGuess == secretWord:
        print("WINNER")
        exit()
    if userGuess in secretWord:
        print("%s is correct." % userGuess)
        for i, letter in enumerate(secretWord):
            if userGuess is letter:
                letterArray[i] = letter
    else:
        print("Incorrect, try again.")
        incorrectArray.append(userGuess)

    # join all elements of letterArray into one element and print.
    letterArray = ''.join([i + "" for i in letterArray])
    print(letterArray)
    if letterArray == secretWord:
        print("WINNER")
        exit()
    # join all elements of incorrectArray into one element and print.
    incorrectArray = ''.join([i + " " for i in incorrectArray])
    print(incorrectArray)


def hangman(secretWord):
    '''
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
    letterArray = ['_'] * len(secretWord)
    incorrectArray = []
    print("The word has %s letters" % len(secretWord))
    numberOfGuesses = 10
    while numberOfGuesses > 0:
        print("You have %s guesses left" % numberOfGuesses)
        getGuessedLetter(secretWord, letterArray, incorrectArray)
        numberOfGuesses = numberOfGuesses - 1
    print('The word was "%s!"' % secretWord)


secretWord = loadWord()
hangman(secretWord)

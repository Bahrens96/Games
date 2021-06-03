# This is the hangman game
# Based on Al Sweigart's hangman found at: https://inventwithpython.com/invent4thed/chapter9.html

import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
    ===''', '''
 +---+
 [O]  |
 /|\  |
 / \  |
    ===''']

words = {'countries': '''united-states canada mexico brazil guyana dominican-republic
        jamaica south-africa zimbabwe egypt tunisia italy spain england france germany poland
        ukraine russia kazakhstan uzbekistan greece turkey israel lebanon iran iraq afghanistan
        pakistan india nepal bangladesh mongolia china japan korea thailand vietnam philippines 
        australia new-zealand indonesia malaysia tahiti kiribati serbia albania montenegro
        algeria slovakia czechia georgia armenia azerbaijan columbia nigeria morocco'''.split(),

         'animals': '''ant baboon badger bat bear beaver camel cat clam cobra cougar
        coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
        lion lizard llama mole monkey moose mouse mule newt otter owl panda
        parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
        skunk sloth snake spider stork swan tiger toad trout turkey turtle
        weasel whale wolf wombat zebra'''.split(),

         'fruits': '''apple banana pear orange dates lime lemon fig mango
         strawberry raspberry blueberry blackberry watermelon kiwi cherry
         grape grapefruit cantaloupe orange tomato olive'''.split(),

         'shapes': '''circle square triangle trapezoid rectangle parallelogram
        rhombus pentagon chevron hexagon octagon decagon dodecagon '''.split(),

         'colors': '''red orange yellow green blue purple violet black brown
         grey white turquoise lime firebrick coral sienna olive bisque cyan
         teal maroon sea-green sky-blue indigo navy magenta fuchsia pink hot-pink
         crimson'''.split(),

         'US_presidents': '''washington adams lincoln roosevelt jackson jefferson
         trump eisenhower kennedy reagan coolidge taft grant madison'''.split(),

         'world_capitals': '''washington-dc ottawa mexico_city brasilia george-town
         santo_domingo kingston cape-town cairo tunis rome lagos harare algiers
         rabat london paris madrid berlin warsaw athens ankara moscow kiev 
         tirana belgrade jerusalem tehran beruit baghdad dubai kabul nur-sultan
         tashkent islamabad new-delhi kathmandu tbilisi yerevan baku bangkok
         beijing hanoi tokyo seoul manila kuala-lumpur ulaanbaatar canberra
         wellington tarawa'''.split()}


def getRandomWord(wordDict):
    # This function returns a random string from the passed dictionary
    # of lists of strings and its key.

    # Second randomly selects a word from the key's list in the dictionary
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

    return [wordDict[wordKey][wordIndex], wordKey]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # Replaces  blanks with correctly
        # guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:  # Show the secret word with spaces in between
        # each letter.
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the
    # player entered a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter or  a hyphen.')
        elif guess in alreadyGuessed:
            print('You already guessed this letter or hyphen. Please guess again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz-' and '-':
            print('Please enter a LETTER or hyphen.')
            print('abcdefghijklmnopqrstuvwxyz -')


        else:
            return guess


def playAgain():
    # This function returns True, if the player wants to play again
    # otherwise it returns False.
    print('Do you want to play again? Please enter yes or no.')
    return input().lower().startswith('y')


print('H A N G M A N')

difficulty = 'X'
while difficulty not in ['E','M','H']:
    print ('Enter difficulty: E- Easy M-Medium H-Hard')
    difficulty = input().upper()


if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is in the set: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # check if the player won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print('Yes! The secret word is " ' + secretWord +
                  '"! You have won! ')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and has lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' +
                  str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses,'
                                             'the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they would like to play again once the game is done

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break

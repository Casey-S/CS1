# Build a working roulette game.  At minimum, this script should
# Complete one round of roulette - but if you're up to the challenge,
# feel free to build a full command line interface through which

import random
random.seed(random)

bank_account = 1000
# bet_amount = 0
bet_color = None
bet_number = None

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


def take_bet():
    Bet_color = raw_input("Enter bet color: ")
    if Bet_color in ["red", "green", "black"]:
        print("Color accepted")
        # return Bet_color
    else:
        print("Invalid color")
        pass

    bet_amount = input("Bet amount: ")

    return Bet_color, bet_amount
    # bet_number = number
    # bet_amount = amount


def roll_ball():
    '''returns a random number between 0 and 37'''
    Number_rolled = random.randint(0, 37)
    return Number_rolled


def check_results():
    '''Compares bet_color to color rolled.'''
    '''Compares bet_number to number_rolled.'''
    number_rolled = roll_ball()
    bet_color = take_bet()
    bet_amount = bet_color[1]

    if number_rolled in red:
        ball_color = "red"

    elif number_rolled in black:
        ball_color = "black"

    elif number_rolled in green:
        ball_color = "green"

    print("Ball landed on %s" % ball_color)

    if bet_color[0] == ball_color:
        print("Color match!")
        color_match = True
        return color_match, bet_amount
    else:
        color_match = False
        return color_match, bet_amount


def payout():
    '''returns total amount won or lost by user based on results of roll. '''
    bet_net = check_results()
    if bet_net[0] is True:
        bet_amount = bet_net[1] * 2
        # bet_amount = bet_amount * 2
        print("You won %s" % bet_amount)
    else:
        pass


def play_game():
    """This is the main function for the game.
    When this function is called, one full iteration of roulette,
    including:
    Take the user's bet.
    Roll the ball.
    Determine if the user won or lost.
    Pay or deduct money from the user accordingly.
    """
    pass


# take_bet()

# check_results()
payout()

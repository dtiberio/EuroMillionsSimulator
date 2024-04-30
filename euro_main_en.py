### import functions
from helper_functions_en import *
from euro_common import *
from datetime import datetime
from art import text2art
from colorama import Fore, Back, Style, init, deinit

#### configuration settings

# initialize the Windows Terminal with colorama
init(autoreset=True)  # reset the Terminal settings after each print()

# possible application states
INITIAL_STATE = 0
LETS_PLAY = 2
BET_PLACED = 4
WINNING_KEY = 6
FINAL_STATE = 8
currentState = INITIAL_STATE

### start the program's main loop

clearTerminal()

print(Fore.BLUE + Back.WHITE + text2art("EuroMillions", font='small'))

while True: # print menu and get user input
    
    # print menu
    print(Fore.BLUE + Back.WHITE + "\n+++  Menu  +++\n")    
    match (currentState):
        case (0):       # INITIAL_STATE
            print("    (P)lay")
            print("    (E)nd")
        case (2):       # LETS_PLAY
            print("    Choose the type of bet:\n")
            print("        (M)anual - choose your numbers")
            print("        (A)utomatic - trust in luck\n")
            print("    (E)nd")
        case (4):       # BET_PLACED
            print("    (D)raw")
            print("    (E)nd")
        case (6):       # WINNING_KEY
            print("    (P)rizes")
            print("    (E)nd")
        case (8):       # FINAL_STATE
            print("    Do you want to end the program?\n")
            print("        (E)nd")
            print("        (P)lay again")

    # get user input
    op = input(Fore.YELLOW + "\nChoose an option and press the corresponding initial letter: ")
    print(Style.RESET_ALL) # colorama requires a print() after an input() to reset the terminal settings

    # check user input (op) to control the currentState of the main loop
    match (op.lower(), currentState):
        
        case ("p", 0):          # INITIAL_STATE
            clearTerminal()
            currentState = LETS_PLAY

        case ("m", 2):          # LETS_PLAY
            # get user's bet
            clearTerminal()
            print(f"{Fore.BLUE}{Back.WHITE}Choose 5 numbers between 1 and {MAX_NUMBERS}:")
            betNumbers = sorted(getUserBet(5, MAX_NUMBERS)) # bet 5 numbers
            
            clearTerminal()
            print(f"{Fore.BLUE}{Back.WHITE}Choose 2 stars between 1 and {MAX_STARS}:")
            betStars = sorted(getUserBet(2, MAX_STARS))  # bet 2 stars

            clearTerminal()
            print(f"\nYour bet is: ", end='')
            printEuroKey(betNumbers, betStars)

            currentState = BET_PLACED

        case ("a", 2):          # LETS_PLAY
            # get random bet
            clearTerminal()

            betNumbers = sorted(getRandomKey(5, MAX_NUMBERS)) # bet 5 numbers
            betStars = sorted(getRandomKey(2, MAX_STARS))  # bet 2 stars
            print(f"\nYour bet is: ", end='')
            printEuroKey(betNumbers, betStars)

            currentState = BET_PLACED

        case ("d", 4):          # BET_PLACED
            # get random draw
            clearTerminal()
            drawTime = datetime.now()
            drawNumbers = getRandomKey(5, MAX_NUMBERS)  # draw 5 numbers
            drawStars = getRandomKey(2, MAX_STARS)   # draw 2 stars

            drawNumbersSorted = sorted(drawNumbers)
            drawStarsSorted = sorted(drawStars)

            currentState = WINNING_KEY

            # Print the key from the draw
            print(f"{Fore.BLUE} {Back.WHITE}\n***  EuroMillions  ***\nDraw Time: {drawTime.strftime('%Y-%m-%d %H:%M:%S')}\n")

            print(f"Winning key: ", end='')
            printEuroKey(drawNumbersSorted, drawStarsSorted)


            print(f"Exit Order: ", end='')
            printEuroKey(drawNumbers, drawStars)

        case ("p", 6):          # WINNING_KEY
            # Result = match between user bet and draw
            matchNumbers = getCommonValues(betNumbers, drawNumbers)
            matchStars = getCommonValues(betStars, drawStars)

            # Prize = match between result and prize list
            numbersCorrect = len(matchNumbers)
            starsCorrect = len(matchStars)

            prize = getPrizeKey(numbersCorrect, starsCorrect)

            clearTerminal()

            print(f"{Fore.BLUE}{Back.WHITE}\nYou matched {numbersCorrect} numbers and {starsCorrect} stars")
            print(f"Result of your bet: ", end='')
            printEuroKey(matchNumbers, matchStars)

            if prize > 0:
                print(f"{Fore.BLUE} {Back.WHITE}\n    *** Congratulations, you won the {prize}th Prize! ***")
            else:
                print(f"\n    Unfortunately, you did not win this time, good luck next time.")

            currentState = INITIAL_STATE

        case ("e", 8):  # FINAL_STATE, exit the loop, bye
            clearTerminal()
            break

        case ("p", 8):  # FINAL_STATE, play again
            clearTerminal()
            currentState = LETS_PLAY

        case ("e", _):  # ask for confirmation before exit
            clearTerminal()
            currentState = FINAL_STATE

        case _:         # any other option is not valid
            print(Fore.RED + "Invalid option. Choose an option and press the corresponding letter:")
            errorTimer(3)  # Pause for 3 seconds to allow the user to read the message
            clearTerminal()


### exit program

print(Fore.BLUE + Back.WHITE + text2art("EuroMillions", font='small'))
print(Fore.YELLOW + "\n    *** Thank you for choosing the games of Santa Casa da Misericórdia. ***\n")

# exit Colorama gracefully
deinit()

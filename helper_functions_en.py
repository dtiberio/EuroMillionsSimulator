import os
import time
from random import randint
from colorama import Fore

def clearTerminal():
    """
    Clear the Terminal in Windows, works with Command Prompt or PowerShell 

    Args:
        None

    Returns:
        None
    """

    if os.name == 'nt':  
        os.system('cls')

def isPositiveInt(num):
    """
    Test if argument num is both an Integer and Positive.

    Args:
        num (int): value to be tested

    Returns:
        bool: Return True if argument is both an Integer and Positive.
    """
    return isinstance(num, int) and num > 0

def isIntInterval(num, a, b):
    """
    Test if argument num is an Integer between [a,b].

    Args:
        num (int): value to be tested
        a (int): lower limit of the interval, inclusive
        b (int): upper limit of the interval, inclusive

    Returns:
        bool: Return True if argument num is an Integer between [a,b].
    """
    if isinstance(num, int) and isinstance(a, int) and isinstance(b, int):
        return a <= num <= b
    else:
        return False

def errorTimer(n):
    """
    Pause for n seconds while printing a countdown to the Terminal.
    If n is not a Positive Integer, it returns without pausing.

    Args:
        n (int): seconds to pause

    Returns:
        None
    """
    if not isPositiveInt(n):
        return
    
    for i in range(n, 0, -1):
        if i == 1:
            print(f"{Fore.RED}{i}", end='')
            time.sleep(1)            
        else:
            print(f"{Fore.RED}{i}...", end='')
            time.sleep(1)

def getRandomKey(n, m):
    """
    Generate a list of n random positive integers between [1,m], must be unique values.
    Uses randint() from random.

    Args:
        n (int): amount of numbers to be generated
        m (int): upper limit of the interval, inclusive

    Returns:
        list: Return a list of length equal to n, or an empty list on error.
    """
    if isPositiveInt(n) and isPositiveInt(m):
        
        keyList = []

        while True:
            if len(keyList) == n:
                return keyList
            else:
                val = randint(1, m)
                if not (val in keyList):    # must be unique values
                    keyList.append(val)
    else: 
        return []

def printList(lista):
    """
    Prints each element in a list followed by a white space.
    If the list is empty, it returns without printing.
    It prints a white space after the last element.
    
    Args:
        lista (list): the list to be printed.
    
    Returns:
        None
    """

    if not lista:
        return
    for elem in lista:
        print(elem, end=' ')

def getUserBet(n, m):
    """
    Retrieve n numbers from the user. The numbers must be positive integers between [1,m] and they must be unique values.
    
    Args:
        n (int): amount of numbers to be retrieved from the user
        m (int): upper limit of the interval, inclusive
    
    Returns:
        list: Return a list of length equal to n, or an empty list on error.
    """

    if not (isPositiveInt(n) and isPositiveInt(m)):
        return []

    keyList = []
    while len(keyList) < n:
        print(f"Current bet: ", end='')
        printList(keyList)
        print()
        try:
            num = int(input(f"Choose number {len(keyList) + 1}, between 1 and {m} without repeating: "))
            if isIntInterval(num, 1, m) and num not in keyList: # must be unique values
                keyList.append(num)
                clearTerminal()
            else:
                print(f"{Fore.RED}\nError: enter a number between 1 and {m} and do not repeat values!")
                errorTimer(3)  # Pause for 3 seconds to allow the user to read the message
                clearTerminal()
        except:
            print(f"{Fore.RED}\nError: only enter numbers between 1 and {m}!")
            errorTimer(3)  # Pause for 3 seconds to allow the user to read the message
            clearTerminal()
    
    return keyList

def getCommonValues(lista1, lista2):
    """
    Search two lists for values in common between them.

    Args:
        lista1 (list): first list, can't be empty
        lista2 (list): second list, can't be empty

    Returns:
        list: Return a sorted list with the values in common, or an empty list.
    """

    if lista1 and lista2:
        lista3 = []
        lista1.sort()
        for item in lista1:
            if item in lista2: # check if item exists in both lists
                if not (item in lista3): # check if item is not a duplicate of a previous item
                    lista3 += [item]  # adds item if it is a common value and it if is not a duplicate
        return sorted(lista3)
    else: 
        return []

def getPrizeKey(numbers, stars):
    """
    Match two numbers against a list of 13 options to check if it's a winning combination.

    Args:
        numbers (int): first number, must be in [0,5]
        stars (int): second number, must be in [0,2]

    Returns:
        int: Return the position on the winning list, between [1,13], or 0 if there's no match.
    """

    if isIntInterval(numbers, 0, 5) and isIntInterval(stars, 0, 2):
        match numbers:
            case 5:
                match stars:
                    case 2:
                        return 1
                    case 1:
                        return 2
                    case 0:
                        return 3
            case 4:
                match stars:
                    case 2:
                        return 4
                    case 1:
                        return 5
                    case 0:
                        return 7
            case 3:
                match stars:
                    case 2:
                        return 6
                    case 1:
                        return 9
                    case 0:
                        return 10
            case 2:
                match stars:
                    case 2:
                        return 8
                    case 1:
                        return 12
                    case 0:
                        return 13
            case 1:
                match stars:
                    case 2:
                        return 11
                    case 1:
                        return 0
                    case 0:
                        return 0
            case 0:
                return 0
    else: 
        return 0

def printEuroKey(lista1, lista2):
    """
    Prints on the Terminal the 2 lists with the format defined by Euromillions. 
    If the list is empty, it prints 0.

    Args:
        lista1 (list): list to be printed, prints 0 if the list is empty
        lista2 (list): list to be printed, prints 0 if the list is empty

    Returns:
        None
    """

    if lista1:
        printList(lista1)
    else: 
        print("0", end=' ')
    if lista2:
        print("+", end=' ')
        printList(lista2)
        print()
    else: 
        print("+ 0\n")

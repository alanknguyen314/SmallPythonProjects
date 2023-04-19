# Bagels, a predictive AI written in Python :)
# It is a deductive logic game where you must guess a number based on clues.

# PROBLEM 1, The big book of small python projects.

import random

NUM_DIGITS = 3;
MAX_GUESSES = 10;

def main():
    print('''
    #############################################################################################
    #############################################################################################
    Bagels, a Deductive Logic Game
    
    I'm thinking of a {}-digit number with no repeated digits. 
    Try to guess what it is. Here are some clues:
    When I say:     That means:
        Pico        One digit is correct but it's in the wrong position.
        Fermi       One digit is correct and it's in the right position.
        Bagels      No digit is correct.
        
    For example, if the secret number was 248 and your guess was 843, the clues would be
    "Fermi Pico".
    #############################################################################################
    #############################################################################################'''.format(NUM_DIGITS));

    while(True):
        secretNum = getSecretNum();
        print("I have thought up a number");
        print("You have {} gueses to get it.".format(MAX_GUESSES));

        numGuesses = 1;

        while numGuesses <= MAX_GUESSES:
            guess = "";
            # KEEP LOOKING FOR CORRECT GUESS
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(numGuesses));
                guess = input("> ");

            clues = getClues(guess, secretNum);
            print(clues);
            numGuesses += 1;

            if guess == secretNum:
                break; # CORRECT, break out loop.
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses!");
                print("The answer was {}.".format(secretNum));

        # Prompt player to play again:
        print("Do you want to play again? (yes/no)");
        if not input("> ").lower().startswith("y"):
            break;
    print("Thanks for playing!");

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list("0123456789");
    random.shuffle(numbers);
    # extract the secret number:
    secretNum = "";
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i]);
    return secretNum;

def getClues(guess, secretNum):
    """Returns a string with the 'Pico', 'Fermi', or 'Bagels' clues for 
    a guess and secret number pair."""
    # base case:
    if guess == secretNum:
        return "You got it!";
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # case when 1st digit is correct
            clues.append("Fermi");
        elif guess[i] in secretNum:
            # case when 1st digit is found but not in right position
            clues.append("Pico");
    if len(clues) == 0: # case when no digit is correctly guessed.
        return "Bagels";
    else:
        # sort the clues into alphabetical order to not give the info about their order away:
        clues.sort();
        # make a single string from the list of string clues:
        return " ".join(clues);

# run main program
# If the program is run (instead of imported), then run the game:
if __name__ == '__main__':
    main();

import time
import random


#user inputs range of letters for game difficulty
def game_size():
    print("Welcome to the guessing game!")

    time.sleep(0.5)

    while True:
        try:
            size = int(input("How smart are you? We're playing from 1 t0 ...?:  "))
            break
        except ValueError:
            print("That's not a number, dummy! Try again...")
            continue

    return size

#game
def game(n):
    previous = {}
    answer = random.randrange(1, n + 1)
    time.sleep(0.5)
    print("Okay. You're playing from 1 to {}".format(n))
    for remaining in range(20, 0, -1):

        #checks to see if the user is out of tries
        if remaining == 0:
            print("Out of tries! You lose!")
            return None
        time.sleep(0.5)

        #guess
        while True:
            try:
                guess = int(input("You've got {} tries left. What's your guess?  ".format(remaining)))
                break
            except ValueError:
                print("Seriously? Numbers only...")
                continue
        if guess in previous:
            print("You already guessed that, ya dingus...")
        else:
            previous.setdefault(guess, 1)

        #check for correct answer
        if guess == answer:
            print("Wow! You're smarter than I thought! Congratulations!")
            return None
        elif guess < answer:
            print("Higher...")
        elif guess > answer:
            print("Lower...")



def main():
    #checks if user wants to play/keep playing
    while True:
        game_prompt = str(input("Do you want to play? (yes/no)  "))
        if game_prompt == 'yes':
            n = game_size()
            game(n)
        elif game_prompt == 'no':
            print("Thanks for playing!")
            break
        else:
            print('Answer "yes" or "no"...')
            continue



main()



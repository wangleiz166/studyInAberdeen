# by Lei Wang
# Student ID：52210762
# 01/10/22 23:53
# github: https://github.com/wangleiz166/studyInAberdeen

# write a program called “guessing_game” without arguments that generates a random number
# between 1 and 100, inclusive. Ask the user to guess the number in a loop until they get it right,
# advising whether the number is too big or too small. You should also keep track of the number


import random

# main function
# parameter: none
# return: none
def guessing_game():
    # random number
    num = random.randint(1, 100)
    # guess times
    times = 1

    while True:
        try:
            # guess number and check
            guess_num = int(input("please guess the number:"))
            # guess right
            if guess_num == num:
                guess_text = "guesses"
                if times == 1:
                    guess_text = "guess"

                print(f"That’s right! You took {times} {guess_text}")
                return

            # guess bigger
            elif guess_num > num:
                print(f"That’s not right, {guess_num} is too big")
            # guess smaller
            else:
                print(f"That’s not right, {guess_num} is too small")

            times += 1
        except:
            print("type wrong! please enter int")


guessing_game()
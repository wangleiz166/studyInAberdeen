import random

number = random.randint(1, 100)
user_number = 0
state = 0

# check the guess_number is singula or plural


def check_singula_plural(i):
    if i == 1:
        print("That's right! you took" + str(i)+"guess")
    else:
        print("That's right! you took" + str(i)+"guesses")


def check_input(user_number):
    try:
        user_number = eval(user_number)
    except:
        print("you input a string, you should input a integer number")
        return -1
    if user_number == "":
        print("you input nothing, please input a number ")
        return -1
    elif type(user_number) == float:
        print("you should input a integer number")
        return -1
    elif user_number > 100 or user_number < 1:
        print("the range is between 1 to 100 and inclusive")
        return -1

    return user_number


def guessing_game():
    i = 0
    while True:
        user_number = input("please input the number which you guess:")
        user_number = check_input(user_number)
        # print(type(state))
        if user_number != -1:
            if user_number > number:
                print(
                    "That's not right,the number you input is too big,please try again.")

            elif user_number < number:
                print(
                    "That's not right,the number you input is too small,please try again.")
            else:
                check_singula_plural(i)
                break
        i += 1

guessing_game()

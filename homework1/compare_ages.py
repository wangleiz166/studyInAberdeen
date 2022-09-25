# by Lei Wang
# Student ID：52210762
# 24/09/22 21:37
#
# Write a function called "compare_ages" without arguments that asks for the user's age and
# responds by saying whether the user is the same age as you, younger or older (and by how
# much)
# For example, if you are 18 years old the program should display on the screen the following:
# "You are one year younger than me." (if input is 17)
# "You are the same age as me." (if input is 18)
# "You are 2 years older than me." (if input is 20)

# Forever 18 years old
my_age = 18

# main function
# parameter: no
# return: no
def compare_ages():
    # get user age
    user_age = input("please enter your age(0-120):")

    # Checking the legality of input
    user_age = check_input(user_age)
    if user_age == -1:
        return

    diff_age = my_age - user_age
    diff_age_abs = abs(diff_age)

    year_str = "years"
    age_type = ""

    # same age
    if diff_age == 0:
        print("You are the same age as me.")
        return

    # younger age
    elif diff_age > 0:
        age_type = "younger"
        if diff_age == 1:
            diff_age = "one"
            year_str = "year"

    # older age
    else:
        age_type = "older"
        if diff_age_abs == 1:
            diff_age_abs = "one"
            year_str = "year"

    print(f"You are {diff_age_abs} {year_str} {age_type} than me.")

# function - Checking the legality of input
# parameter: user_age int
# return: user_age int
def check_input(user_age):
    # check not ""
    if user_age == "":
        print("Age cannot be empty ! Please re-enter:")
        return -1

    try:
        user_age = eval(user_age)
    except:
        print("Age cannot be string type ! Please re-enter")
        return -1

    # must be int
    if type(user_age) != int:
        print("Age cannot be float type ! Please re-enter:")
        return -1
    #must (0<age<120)
    if user_age < 0 or user_age > 120:
        print("Wrong age range ! Please re-enter in (0-120):")
        return -1

    return user_age

compare_ages()

# by Lei Wang
# Student ID：52210762
# 24/09/22 23:53
# github: https://github.com/wangleiz166/studyInAberdeen

# Write a program called ‘tempConverter.py’ to convert temperatures to and from Celsius,
# Fahrenheit. To accomplish this, you need to create the following two functions that accept a
# temperature degree as the only argument:
# celToFah(temperature)
# FahToCel(temperature)
# In addition, you need to create another function called mainProgram() that asks the user for a
# temperature scale (1 for Celsius and 2 for Fahrenheit) and returns the converted temperature to
# the user. (15 Marks)
# For example, if the user selects Celsius as the input temperature scale, the output would be:
# >>> The temperature xxx in Celsius is equivalent to xxx in Fahrenheit.
# Similarly, if the user selects Fahrenheit as the input temperature scale, the output would be:
# >>> The temperature xxx in Fahrenheit s equivalent to xxx in Celsius.

# main function
# parameter: no
# return: no
def mainProgram():
    temperature_scale = input("please enter temperature scale (1 for Celsius and 2 for Fahrenheit):")
    temperature = input("please enter temperature:")

    # Checking the legality of input
    temperature_scale, temperature = checkInput(temperature_scale, temperature)
    if temperature_scale == -1:
        return

    if temperature_scale == 1:
        # check Celsius temperature range
        if temperature >= -273.15:
            fah_temperature = celToFah(temperature)
            #print(f"The temperature {temperature} in Celsius is equivalent to {round(fah_temperature,2)} in Fahrenheit")
            print(
                f"The temperature {temperature} in Celsius is equivalent to {fah_temperature} in Fahrenheit")

        else:
            print("Celsius temperature Must be (temperature >=-273.15) Please re-enter :")
            return
    else:
        # check Fahrenheit temperature range
        if temperature >= -459.67:
            cel_temperature = FahToCel(temperature)
            print(
                f"The temperature {temperature} in Fahrenheit s equivalent to {cel_temperature} in Celsius")
        else:
            print("Celsius temperature Must be (temperature >=-459.67) Please re-enter :")
            return

# function - Checking the legality of input
# parameter: temperature_scale int , temperature int
# return: user_age int
def checkInput(temperature_scale, temperature):
    # check input not empty
    if temperature_scale == "":
        print("temperature scale cannot be empty ! Please re-enter:")
        return -1, 0

    if temperature == "":
        print("temperature cannot be empty ! Please re-enter:")
        return -1, 0

    # check temperature_scale not string
    try:
        temperature_scale = eval(temperature_scale)  # int or float
    except:
        print("temperature scale cannot be string type ! Please re-enter")
        return -1, 0

    # check temperature_scale not float
    if type(temperature_scale) != int:
        print("temperature scale cannot be float type ! Please re-enter:")
        return -1, 0

    # check temperature_scale range
    if temperature_scale not in [1, 2]:
        print("Wrong temperature_scale range ! Please re-enter(1,2):")
        return -1, 0

    # check temperature not string
    try:
        temperature = eval(temperature)
    except:
        print("temperature cannot be string type ! Please re-enter")
        return -1, 0

    return temperature_scale, temperature

# function make Celsius temperature to Fahrenheit temperature
# F = (C*1.8)+32
# parameter: temperature int / float
# return: fah_value int / float
def celToFah(temperature=0):
    fah_value = temperature * 1.8 + 32
    # format eg:50.0 => 50 or 33.333333333333333333 => 33.3333 or 50.199998 => 50.2
    fah_value = '{:g}' .format(fah_value)
    return fah_value

# function make Fahrenheit temperature to Celsius temperature
# C = F-32/1.8
# parameter: temperature int / float
# return: cel_value int / float
def FahToCel(temperature=0):
    cel_value = (temperature - 32) / 1.8
    # format eg:50.0 => 50 or 33.333333333333333333 => 33.3333 or 50.199998 => 50.2
    cel_value = '{:g}' .format(cel_value)
    return cel_value


mainProgram()

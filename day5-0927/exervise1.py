list = ['a','e','i','o','u']

def withoutVowels(str):
    new_str = ""
    for i in range(len(str)):
        if str[i] not in list:
           new_str = new_str + str[i]
        else: 
           new_str = new_str + " "

    return new_str

print(withoutVowels("i do not like vowels!"))
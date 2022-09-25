# 编写一个程序，从用户的英文字母中读取一个字母。 如果字母是元音（a，e，o，i，u），
# 那么它应该通知用户它是一个元音。 如果字母是 (y)，
# 那么它应该通知用户有时它是元音，有时不是。 否则为辅音

word = input("enter word:")

#获取第一个字母
first_word = word[0]

vowel_list = ['a','e','i','o','u']

if (first_word in vowel_list):
    print("it is vowel")
elif first_word == "y":
    print("y it is vowel")
else:
    print("it is consonant")    



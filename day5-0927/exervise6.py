def printDown(text):
    i = 0
    while i < len(text):
      char = text[i]
      print(char)
      i+= 1

def printUp(text):
    str = ""
    for i in range(len(text)):
       print(len(text) - i) 
       str += text[len(text) - i -1] 

    print(str) 

printUp("abcd")      


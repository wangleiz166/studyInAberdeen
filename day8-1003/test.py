from Crypto.Util.Padding import *
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import StringIO 

deskey = get_random_bytes(8)

cipher = DES.new(deskey, DES.MODE_CBC)

plaintext = "DES Algorithm Implementation"

ciphertext = cipher.iv + cipher.encrypt(pad(plaintext, 8))

print ("Initialisation Vector: %r" %cipher.iv)
print ("Encrypted: %r" %ciphertext)

#For decyprtion, we first have to read the iv out of the message and 
#then decrypt the message. 

print ("Lets decrypt the message now")

sio = StringIO.StringIO(ciphertext) 

iv = sio.read(8)
ciphertext = sio.read()

cipher = DES.new(deskey, DES.MODE_CBC, iv)

plaintext = unpad(cipher.decrypt(ciphertext),8)

print ("Plaintext: %r" %plaintext)

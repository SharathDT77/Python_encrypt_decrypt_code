# Python encryption program
# Punctuation --> provides a predefined string containing all the characters commonly considered punctuation


import random
import string
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)
print(f"chars: {chars}")
print(f"key:   {key}")

#Encryption

plain_text = input("Enter a message to encrpyt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]


print(f"Original message:  {plain_text}")
print(f"Encrypted message: {cipher_text}")

#Decryption

ciper_text = input("Enter a message to decrpyt: ")
plain_text = ""

for letter in ciper_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {plain_text}")
print(f"Original message:  {cipher_text}")
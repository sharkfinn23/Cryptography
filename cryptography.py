"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
code=str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
while code not in ["e","d","q"]:
    print("Did not understand command, try again.")
    code=str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
if code == "q":
    print("Goodbye! ")
while code == "e":
    key=list(input("Key: ")
    message=input("Message: ")
    for x in range (0, len(message)):
        message[x]=associations.find(message[x])
    for x in range (0, len(key)):
        key[x]=associations.find(key[x])
    while len(key)<len(message)
    
if code == "d":
    key=input("Key: ")



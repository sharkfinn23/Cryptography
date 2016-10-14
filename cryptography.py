"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
enumlist = []
ekeynumlist = []
enewnums = []
eend = []
dnumlist = []
dkeynumlist = []
dnewnums = []
dend = []
while command != "q":
    if command == "e":
        emessage = input("Message: ")
        ekey = input("Key: ")
        eeekey = ekey
        while len(ekey) < len(emessage):
            ekey = ekey + eeekey
        for x in emessage:
            enumlist.append(associations.find(x))
        for y in ekey:
            ekeynumlist.append(associations.find(y))
        ezip = list(zip(enumlist, ekeynumlist))
        for a in ezip:
            if a[0]+a[1] < len(associations):
                enewnums.append(a[0] + a[1])
            else:
                enewnums.append(a[0] + a[1] - len(associations))
        for i in enewnums:
            eend.append(associations[i])
        print(''.join(eend))
        enumlist = []
        ekeynumlist = []
        enewnums = []
        eend = []
    if command == "d":
        dmessage = input("Message: ")
        dkey = input("Key: ")
        deekey = dkey
        while len(dkey) < len(dmessage):
            dkey = dkey + deekey
        for x in dmessage:
            dnumlist.append(associations.find(x))
        for y in dkey:
            dkeynumlist.append(associations.find(y))
        dzip = list(zip(dnumlist, dkeynumlist))
        for a in dzip:
            if a[0]-a[1] >= 0:
                dnewnums.append(a[0] - a[1])
            else:
                dnewnums.append(a[0] - a[1] + len(associations))
        for i in dnewnums:
            dend.append(associations[i])
        print(''.join(dend))
        dnumlist = []
        dkeynumlist = []
        dnewnums = []
        dend = []
    if command != "d" and command != "e" and command !="q":
        print("Did not understand command, try again.")
    command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
if command == "q":
    print("Goodbye!")
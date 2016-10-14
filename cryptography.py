"""
cryptography.py
Author: finn
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
enumbers = []
ekeynumbers = []
enewnumbers = []
eend = []
dnumbers = []
dkeynumbers = []
dnewnumbers = []
dend = []

while command != "q":
    
    if command == "e":
        emessage = input("Message: ")
        ekey = input("Key: ")
        eeekey = ekey

        while len(ekey) < len(emessage):
            ekey = ekey + eeekey

        for x in emessage:
            enumbers.append(associations.find(x))
        for y in ekey:
            ekeynumbers.append(associations.find(y))
             
        ezip = list(zip(enumbers, ekeynumbers)
        
        for a in ezip:
            if a[0]+a[1] < len(associations):
                enewnumbes.append(a[0] + a[1])
            else:
                enewnumbers.append(a[0] + a[1] - len(associations))
        
        for i in enewnumbers:
            eend.append(associations[i])
            
        print(''.join(eend))

        enumbers = []
        ekeynumbers = []
        enewnumbers = []
        eend = []
    if command == "d":
        dmessage = input("Message: ")
        dkey = input("Key: ")
        deekey = dkey
        while len(dkey) < len(dmessage):
            dkey = dkey + deekey
        for x in dmessage:
            dnumbers.append(associations.find(x))
        for y in dnumbers:
            dkeynumbers.append(associations.find(y))
             
        dzip = list(zip(dnumbers, dkeynumbers))
        
        for a in dzip:
            if a[0]-a[1] >= 0:
                dnewnumbers.append(a[0] - a[1])
            else:
                dnewnumbers.append(a[0] - a[1] + len(associations))

        for i in dnewnums:
            dend.append(associations[i])
            
        print(''.join(dend))
        
        dnumbers = []
        dkeynumbers = []
        dnewnumvers = []
        dend = []

    
    if command != "d" and command != "e" and command !="q":
        print("Did not understand command, try again.")
        
    command = input("Enter e to encrypt, d to decrypt, or q to quit: ")

if command == "q":
    print("Goodbye!")

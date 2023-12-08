
ciphertext = open("ciphertext.txt","r").read()
ciphertext = ciphertext.replace(" ","")
print(ciphertext)
print(len(ciphertext))
key = 3
factors = [1, 2, 3, 4, 6, 8, 12, 16, 23, 24, 32, 46, 48, 69, 92, 96, 138, 184, 276, 368, 552, 736, 1104, 2208]
possKeys = []
for each in factors:
    if (each-2)%2==0:
        possKeys.append((each-2)//2+2)
print(possKeys)

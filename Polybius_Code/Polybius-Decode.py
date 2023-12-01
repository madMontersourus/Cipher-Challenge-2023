import numpy as np
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
key = "LETR"+alphabet
keySet = "".join(dict.fromkeys(key))
print(keySet)
strArr=np.array(list(keySet)).reshape(5,5)
polyDict = {}
for i in range(0,5):
    for j in range(0,5):
        polyDict[f"{i+1}{j+1}"] = strArr[i][j]

ciphertext = open("ciphertext.txt","r").read()
ciphertext = ciphertext.replace(" ","")
plaintext = "" 
n = 2
ctArr = [ciphertext[i:i+n] for i in range(0, len(ciphertext), n)]
print(ctArr)
for each in ctArr:
    plaintext += polyDict[each]
print(plaintext)
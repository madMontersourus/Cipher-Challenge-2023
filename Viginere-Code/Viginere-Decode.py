import numpy as np
import json
ciphertext = open("ciphertext.txt","r").read()
ciphertext = ciphertext.replace(" ","")
keylen = 3
A = 65
EngFreq = dict(json.loads(open("frequency.json","r").read()))
sortedEngFreq = dict(sorted(EngFreq.items(), key=lambda item: item[1]))
for i in range(keylen):
    testString = (ciphertext[i::keylen])
    best_shift = 0
    best_score = float("inf")
    for i in range(26):
        tempFreq = EngFreq
        plaintext = ""
        for each in testString:
            plaintext += chr((ord(each)+i-A)%26+A)
        unique, counts = np.unique(np.array(list(plaintext)), return_counts=True)
        freq = dict(zip(unique, counts/len(plaintext)))
        sortedFreq = dict(sorted(freq.items(), key=lambda item: item[1]))
        score = sum(abs(sortedFreq.get(char, 0) / len(ciphertext) * 100 - sortedEngFreq[char]) for char in sortedEngFreq)
        if score < best_score:
            best_score = score
            best_shift = i
    plaintext = ""
    for each in testString:
        plaintext += c ((ord(each)+best_shift-A)%26+A)
    print(plaintext)
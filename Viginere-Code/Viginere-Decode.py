import numpy as np
import json
freq = dict(json.loads(open("frequency.json","r").read()))

def score_plaintext_weighted(plaintext):
    total_score = 0
    for char in plaintext:
        total_score += freq[char]
    return total_score

def CaeserCipher(ciphertext):
    A = 65
    score = 0
    for i in range(1, 27):
        plaintextTemp = ""
        for each in ciphertext:
            plaintextTemp += chr((ord(each)+i-A)%26+A)
        scoreTemp = score_plaintext_weighted(plaintextTemp)
        if scoreTemp > score:
            score = scoreTemp
            shift = i
            plaintext = plaintextTemp
    return plaintext, shift, score

ciphertext = open("ciphertext.txt","r").read()
ciphertext = ciphertext.replace(" ","")

factors = []
for i in range(1, len(ciphertext)+1):
    if len(ciphertext)%i==0:
        factors.append(i)
print(factors)

keylen = 4
answer = []
for i in range(keylen):
    testString = (ciphertext[i::keylen])
    plaintext = CaeserCipher(testString)
    answer.append([*plaintext[0]])
answerFinal = ""
for i in range(len(answer[0])-1):
    for each in answer:
        answerFinal += each[i]
print(answerFinal)

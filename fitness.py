'''library imports'''
import json
import math

#processes the text (removes non-alphabetic characters, capitalises everything)
def process(text):
    NewText = ""
    for each in text:
        if each.isalpha():
            NewText += each.upper()
    return(NewText)


#takes text and length of tetragram (1 for monogram, 4 for quadgram) and returns dictionary of frequencies (not ordered)
def tetragramFrequency(text,length):
    TetFreq = {}
    for i in range (len(text)-(length-1)):
        if text[i:i+length] in TetFreq:
            TetFreq[text[i:i+length]] += 1
        else:
            TetFreq.update({f"{text[i:i+length]}":1}) 
    for each in TetFreq:
        TetFreq[each] = TetFreq[each]/len(text)
    return TetFreq

#takes monogram frequency, closer to 0, closer to English
def Xstat(text,frequency):
    monograms = tetragramFrequency(text,1)
    X = 0
    for each in monograms:
        X += ((monograms[each]-frequency[each])**2)/frequency[each]
    return(X)

#required for angle fitness
def dotProduct(vector1,vector2):
    product = 0
    for each in vector1:
        product += vector1[each]*vector2[each]
    return product

#takes monogram frequency, value will be between 0 and 1, closer to 0, closer to Enlish
def angleFitness(text,frequency):
    monograms = tetragramFrequency(text,1)
    cosTheta = dotProduct(monograms,frequency)/math.sqrt(dotProduct(monograms,monograms)*dotProduct(frequency,frequency))
    Theta = math.acos(cosTheta)
    return Theta

#takes tetragram frequency (4 with partner json file), closer to 0, closer to English
def tetragramFitness(text,frequency):
    tetragrams = tetragramFrequency(text,4)
    fitness = 0
    for each in tetragrams:
        if each in frequency:
            fitness += math.log10(frequency[each])
    fitness /= len(tetragrams)
    fitness = 10**fitness
    return fitness

'''file imports'''
ciphertext = process(open("ciphertext.txt","r").read())
EngTet = dict(json.loads(open("English-frequency.json","r").read()))
EngMon = dict(json.loads(open("frequency.json","r").read()))
English = process(open("english.txt","r").read())

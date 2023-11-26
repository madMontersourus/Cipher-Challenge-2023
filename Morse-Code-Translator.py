import json
morseDict = dict(json.loads(open("Morse-Code-Dict.json","r").read()))
morse = open("morse-code.txt","r").read()
morse = morse.split(" ")
ciphertext = ""
for each in morse:
    ciphertext += 

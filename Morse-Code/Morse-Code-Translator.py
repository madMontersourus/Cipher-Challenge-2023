import json
morseDict = dict(json.loads(open("Morse-Code/Morse-Code-Dict.json","r").read()))
morse = open("Morse-Code/morse-code.txt","r").read()
morse = morse.split(" ")
ciphertext = ""
for each in morse:
    ciphertext += morseDict[each]
open("ciphertext.txt","w").write(ciphertext)

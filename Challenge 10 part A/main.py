ciphertext = open("ciphertext.txt","r").read()
ciphertext = ciphertext.replace(" ","")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ctarr = []
ctVect = []
ptarr = []
ptstr = ""
mat = [[2,25],[25,1]]
for each in ciphertext:
    ctarr.append(alphabet.index(each)+1)
start = 0
end = len(ctarr) 
step = 2
for i in range(start, end, step): 
    x = i 
    ctVect.append(ctarr[x:x+step])
for each in ctVect:
    for i in range(0,2):
        num = (each[0]*mat[i][0]+each[1]*mat[i][1])%26
        if i == 0:
            string = alphabet[num-1]
        elif i == 1:
            string = alphabet[num]
        ptstr += string
        
print(ptstr)
fp="Shikher-jain/ALL IN ONE/01START/07Files/advData.txt"


fd = open(fp,'r')
txt = fd.read()
fd.close()

print(txt)


for i in range(7,19):
    pattern = "[" + str(i) + "]"
    txt = txt.replace(pattern , "")
    
print(txt)


for i in "!@#$%^":
    txt = txt.replace(i , "")
print(txt)



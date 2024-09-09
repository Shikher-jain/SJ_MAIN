fp="Shikher-jain/ALL IN ONE/01START/07Files/data.txt"


fd = open(fp,'r')
txt = fd.read()
fd.close()
print(txt)


per = txt.split("\n\n")
print(per)
print(len(per))


lines = txt.split(".")
print(len(lines[:-1]))

words = txt.split(" ")
print(len(words))



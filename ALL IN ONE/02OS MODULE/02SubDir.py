import os
import sys
import time
n = 'C:/My Programs/Shikher-jain/ALL IN ONE/02OS MODULE/test'
m="test"
if os.path.exists("C:/My Programs/Shikher-jain/ALL IN ONE/02OS MODULE/test"):
    pass
else:
    os.mkdir(n)
for i in range(1000):
    name = n+"/" + m + " " + str(i+1)# i=0 GFG/GFG1 
                                    #  i=50 GFG/GFG50
    os.mkdir(name)

time.sleep(10)
for i in range(1000):
    name = n+"/" + m + " " + str(i+1)# i=0 GFG/GFG1 
                                    #  i=50 GFG/GFG50
    os.rmdir(name)
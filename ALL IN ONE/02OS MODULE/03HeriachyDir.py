import os
hub = 'C:/My Programs/Shikher-jain/ALL IN ONE/02OS MODULE/hub'
master="master"
slave="slave"
if os.path.exists(hub):
    pass
else:
    os.mkdir(hub)

# os.mkdir(master)
n = 5
m = 50
for i in range(n):
    name = hub +'/'+ master + " " + str(i+1)
    if os.path.exists(name):
        pass
    else:
        os.mkdir(name)
    for j in range(m):
        name = hub +'/'+ master + " " + str(i+1) +"/"+ slave + " " + str(j+1) 
        if os.path.exists(name) :
            pass
        else:
            os.mkdir(name)        
print(n*m + n + 1)


# os.remove(hub)
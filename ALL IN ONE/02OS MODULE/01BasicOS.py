import os
import stat

# print(os.__dict__)

# print(os.path.exists("Shikher-jain/ALL IN ONE/02OS MODULE/01BasicOC.py"))
# fp=input("Enter Filename to make directory : ")
# os.mkdir(f'Shikher-jain/ALL IN ONE/02OS MODULE/{fp}')
# print(os.path.exists(f"Shikher-jain/ALL IN ONE/02OS MODULE/{fp}"))

"Shikher-jain/ALL IN ONE/02OS MODULE"

for i in os.listdir("Shikher-jain/ALL IN ONE/02OS MODULE"):    
    if i != '.DS_Store':  ##System
        print(i)


print('''
os.F_OK: Checks if the path exists.
os.R_OK: Checks if the path is readable.
os.W_OK: Checks if the path is writable.
# os.X_OK: Checks if the path is executable.
# ''')

# # Check access with os.F_OK
# p="C:/My Programs/Shikher-jain/text.txt"
# print("path: ",os.path.exists(p))
# path1 = os.access(p, os.F_OK)
# print("Does the path exists:", path1)
# # Check access with os.R_OK
# path2 = os.access(p, os.R_OK)
# print("Access to read the file:", path2)
# # Check access with os.W_OK
# path3 = os.access(p, os.W_OK)
# print("Access to write to file:", path3)
# # Check access with os.X_OK
# path4 = os.access(p, os.X_OK)
# print("Can path be executed:", path4)


#Print current working dir
print("Current directory:" , os.getcwd())

#Create a new dir
if os.path.exists("Shikher-jain/ALL IN ONE/02OS MODULE/mydir"):
    pass
else:
    os.mkdir("Shikher-jain/ALL IN ONE/02OS MODULE/mydir")


#Change current working dir
os.chdir("Shikher-jain/ALL IN ONE/02OS MODULE/mydir")

#Print current working directory
print("Current directory now:" , os.getcwd())

# os.chflags("/tmp/test.txt", stat.UF_IMMUTABLE)  #UNIX

'''
Syntax
os.chflags(path, flags, follow_symlinks)

path - Required. A file path to set the flag
flags - Required. One or more stat module constants which might be in combination (bitwise OR),
stat.UF_NODUMP -     Do not dump the file
stat.UF_IMMUTABLE -  File may not be changed(read-only)
stat.UF_APPEND -     File may only be appended to
stat.UF_OPAQUE -     Directory is opaque, view through a union stack
stat.UF_NOUNLINK -   The file may not be renamed or deleted
stat.UF_COMPRESSED - The file is stored compressed (Mac OS X 10.6+)
stat.UF_HIDDEN -     The file should not be displayed in a GUI (Mac OS X 10.5+)
stat.SF_ARCHIVED -   The file may be archived
stat.SF_IMMUTABLE    The file may not be changed
stat.SF_APPEND -     The file may only be appended to
stat.SF_NOUNLINK -   The file may not be renamed or deleted
stat.SF_SNAPSHOT -   The file is a snapshot file
'''


#Change the mode of path
os.chmod("C:/My Programs/Shikher-jain/ALL IN ONE/02OS MODULE/tempCodeRunnerFile.py", stat.S_IWRITE)

import os
import sys
import stat

# Set given file read by the owner.
os.chmod("C:/My Programs/Shikher-jain/ALL IN ONE/02OS MODULE/tempCodeRunnerFile.py", stat.S_IREAD)
print("File can be read only by owner.")

# Set given file read by others.
os.chmod("C:/My Programs/Shikher-jain/ALL IN ONE/02OS MODULE/tempCodeRunnerFile.py", stat.S_IROTH)
print("File access changed, can be read by others now.")

print(os.cpu_count())   #  $ means cpu in this PC



'''                  UNIX
# File path 

# Print the current owner id 
# and group id of the 
# specified file path 

# os.stat() method will return a 
# 'stat_result’ object of 
# ‘os.stat_result’ class whose 
# 'st_uid' and 'st_gid' attributes 
# will represent owner id and group id 
# of the file respectively 
print("Owner id of the file:", os.stat(path).st_uid) 
print("Group id of the file:", os.stat(path).st_gid) 


# Change the owner id and 
# the group id of the file 
# using os.chown() method 
uid = 2000
gid = 2000
os.chown(path, uid, gid) 
print("\nOwner and group id of the file changed") 


# Print the owner id 
# and group id of the file 
print("\nOwner id of the file:", os.stat(path).st_uid) 
print("Group id of the file:", os.stat(path).st_gid) 

'''
#print the owner id and group id of file
# print (os.chown( "C:/My Programs/Shikher-jain/ALL IN ONE/02OS MODULE/tempCodeRunnerFile.py", 100, 2000))
pathh = "C:/My Programs/Shikher-jain/ALL IN ONE/02OS MODULE/mydir.txt"

fd = os.open(pathh, os.O_RDWR | os.O_CREAT)
# Write a string
os.write(fd, b"This is test data")
# Close opened file
os.close(fd)



# #Abort the current running process
print ("Process abort after printing this line")
os._exit(1);os.abort()
print ("Process abort before printing this line")
print(os.getsize("Shikher-jain/ALL IN ONE/02OS MODULE"))
for i in range(10):
    print(i)
    if i == 2:
        break
print()
# Python program to
# demonstrate break statement
  
s = 'geeksforgeeks'
# Using for loop
for letter in s:
  
    print(letter)
    # break the loop as soon it sees 'e'
    # or 's'
    if letter == 'e' or letter == 's':
        break
  
print("Out of for loop"    )
print()
  
i = 0
  
# Using while loop
while True:
    print(s[i])
  
    # break the loop as soon it sees 'e'
    # or 's'
    if s[i] == 'e' or s[i] == 's':
        break
    i += 1
  
print("Out of while loop ")


num = 0
for i in range(10):
    num += 1
    if num == 8:
        break
    print("The num has value:", num)
print("Out of loop")



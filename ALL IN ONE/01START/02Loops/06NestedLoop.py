x = [1, 2]
y = [4, 5]
  
for i in x:
  for j in y:
    print(i, j)


# Running outer loop from 2 to 3
  
for i in range(2, 4):
  
    # Printing inside the outer loop
    # Running inner loop from 1 to 10
    for j in range(1, 11):
  
        # Printing inside the inner loop
        print(i, "*", j, "=", i*j)
    # Printing inside the outer loop
    print()

# Initialize list1 and list2
# with some strings
list1 = ['I am ', 'You are ']
list2 = ['healthy', 'fine', 'geek']
  
# Store length of list2 in list2_size
list2_size = len(list2)
  
# Running outer for loop to
# iterate through a list1.
for item in list1:
    
    # Printing outside inner loop
    print("start outer for loop ")
    # Initialize counter i with 0
    i = 0
    # Running inner While loop to
    # iterate through a list2.
    while(i < list2_size):
        
        # Printing inside inner loop
        print(item, list2[i])
        # Incrementing the value of i
        i = i+1
    # Printing outside inner loop
    print("end for loop ")

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

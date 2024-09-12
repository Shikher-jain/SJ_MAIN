import array
import random


MAX_LIMIT=128
def display(tr):
    password=""
    for i in tr:
        password+=i
    print(password)  #Final PassWord

#Minimum lenght of password is 4 which means 3 < l < MAX_LIMIT
l=int(input(f"Enter The Lenght Of Password (3 < Lenght < {MAX_LIMIT}): "))  
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lower_chr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
upper_chr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
spe_symbols=['`','~','!','@','#','$','%','^','&','*','(',')','_','-','=','+','[','{',']','}','\\','|',';',':','"',"'",'/','?','.','>',',','>']

# print(len(digits)+len(lower_chr)+len(upper_chr)+len(spe_symbols))
combination = digits + upper_chr + lower_chr + spe_symbols 

rand_digit = random.choice(digits) 
rand_upper = random.choice(upper_chr) 
rand_lower = random.choice(lower_chr) 
rand_symbol = random.choice(spe_symbols) 
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol 

    # print(temp_pass)

if(l>MAX_LIMIT):
    print(f"Too Big PassWord\nEnter Length Again:\n(i.e. : <= {MAX_LIMIT})")

elif(l==4):
    tr=array.array("u",temp_pass)
    random.shuffle(tr) #shuffling makes pas09sword more strong
    # random.shuffle(tr) #if you want more than apply more shuffles
    display(tr)

elif(l>4):
    for for_iterate in range(l-4):
        temp_pass+=random.choice(combination)

        # print(temp_pass)
        tr=array.array("u",temp_pass)
        random.shuffle(tr) #shuffling makes password more strong
        # random.shuffle(tr) #if you want more than apply more shuffles
    display(tr)

else:
    print("Invalid Lenght\nKindly Enter Valid Length\n(i.e. : >= 4)")

import sys 
print('''
Python print() function prints the message to the screen or any other standard output device.

Syntax: 

print(value(s), sep= ' ', end = '\n', file=file, flush=flush)

Parameters: 

value(s) : Any value, and as many as you like. Will be converted to a string before printed
sep=’separator’ : (Optional) Specify how to separate the objects, if there is more than one.Default :’ ‘
end=’end’: (Optional) Specify what to print at the end.Default : ‘\n’
file : (Optional) An object with a write method. Default :sys.stdout
flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False

''')
print(")~~~(""hello","this","is","hello","world",sep=")~~~(", end=")~~~( ",file=sys.stdout,flush=True)
print("\n\nGeeksforGeeks \n is best for DSA Content.")

# This line will automatically add a new line before the
# next print statement
print ("GeeksForGeeks is the best platform for DSA content")
 
# This print() function ends with "**" as set in the end argument.
print ("GeeksForGeeks is the best platform for DSA content", end= "**")
print("Welcome to GFG")
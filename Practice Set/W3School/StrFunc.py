'''
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning
'''

str="Hi shd {p:.2f}"
point = {'x':4,'y':-5}
txt = "Hello  a Sam!"


print("str.capitalize()	 ",str.capitalize()	)   
print("str.casefold()    ",str.casefold()      )
print("str.center(12)	 ",str.center(12)	    )   
print("str.count('s') 	 ",str.count('s') 	    )   
print("str.encode()    	 ",str.encode()    	)   
print("str.endswith('d') ",str.endswith('d')	    ) 
print("str.expandtabs()	 ",str.expandtabs()	)   
print("str.find('4')     ",str.find('4')	        ) 
print("str.format(p=18)	 ",str.format(p=18)	    )   
print("{x} {y}'.format_map(point)",'{x} {y}'.format_map(point))   
print("str.index('s')	     ",str.index('s')	        )
print("str.isalnum()     ",str.isalnum()	    )  
print("str.isalpha()     ",str.isalpha()	    )  
print("str.isascii()     ",str.isascii()	    )  
print("str.isdecimal()   ",str.isdecimal()	    )
print("str.isdigit()     ",str.isdigit()       )
print("str.isidentifier()",str.isidentifier()  )
print("str.islower()	 ",str.islower()	    )  
print("str.isnumeric()	 ",str.isnumeric()	    )
print("str.isprintable() ",str.isprintable()	)  
print("str.isspace()     ",str.isspace()	    )  
print("str.istitle()	 ",str.istitle()	    )  
print("str.isupper()     ",str.isupper()	    )  
print("'~'.join(str)	 ",'~'.join(str)	        ) 
print("'s'.ljust()	     ",'s'.ljust(10)	        )
print("'s'.ljust()	     ",'s'.ljust(10,'!')	        )
print("str.lower()	     ",str.lower()	        )
print("str.lstrip()	     ",str.lstrip()	    )   
print("txt.translate(str.maketrans(\"S\", \"P\"))", txt.translate(str.maketrans("S", "P")))
print("txt.partition(\"bananas\")",txt.partition("bananas")	    )
print("txt.partition(\"S\")	  	 ",txt.partition("S")	    )
print("txt.replace('S','R')	 ",txt.replace('S','R')	    )  
print("txt.rfind('a')	     ",txt.rfind('a')	        )
print("txt.rindex('a')    	 ",txt.rindex('a')    	)   
print("str.rjust(10)	     ",str.rjust(10)	        )
print("str.rjust(10,'!')	     ",str.rjust(10,'!')	        )
print("str.rpartition('S')  ",str.rpartition('S')    )
print("str.rsplit()	     ",str.rsplit()	    )   
print("str.rstrip()	     ",str.rstrip()	    )   
print("str.split()       ",str.split()         )
print("str.splitlines()	 ",str.splitlines()	)   
print("str.startswith('H')	 ",str.startswith('H')	)   
print("str.strip()       ",str.strip()         )
print("str.swapcase()	 ",str.swapcase()	    ) 
print("str.title()       ",str.title()         )
# print("str.translate()   ",str.translate()     )   #82
print("str.upper()	     ",str.upper()	        )
print("str.zfill(55)	     ",str.zfill(20)	        )
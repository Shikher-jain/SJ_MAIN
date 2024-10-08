import tkinter as tk

# Creating the GUI window
root = tk.Tk()
root.title("Simple Calculator")

# Entry field for displaying the result
e = tk.Entry(root, width=35, borderwidth=5, font=("Arial", 24), fg="white", bg="black")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to update the entry field
def button_click(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))

# Function to clear the entry field
def button_clear():
    e.delete(0, tk.END)

# Function to perform calculations
def button_equal():
    try:
        current = e.get()
        e.delete(0, tk.END)
        e.insert(0, eval(current))
    except:
        e.insert(0, "Error")

# Function to delete the last character
def button_backspace():
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, current[:-1])

# Creating the number buttons
button_1 = tk.Button(root, text="1", padx=39, pady=20, font=("Arial", 18), command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=39, pady=20, font=("Arial", 18), command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=39, pady=20, font=("Arial", 18), command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=39, pady=20, font=("Arial", 18), command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=39, pady=20, font=("Arial", 18), command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=39, pady=20, font=("Arial", 18), command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=39, pady=20, font=("Arial", 18), command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=39, pady=20, font=("Arial", 18), command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=39, pady=20, font=("Arial", 18), command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=39, pady=20, font=("Arial", 18), command=lambda: button_click(0))

# Creating the operator buttons
button_add = tk.Button(root, text="+", padx=35, pady=20, font=("Arial", 18), command=lambda: button_click("+"))
button_subtract = tk.Button(root, text="-", padx=35, pady=20, font=("Arial", 18), command=lambda: button_click("-"))
button_multiply = tk.Button(root, text="*", padx=35, pady=20, font=("Arial", 18), command=lambda: button_click("*"))
button_divide = tk.Button(root, text="/", padx=35, pady=20, font=("Arial", 18), command=lambda: button_click("/"))
button_equal = tk.Button(root, text="=", padx=91, pady=20, font=("Arial", 18), command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, font=("Arial", 18), command=button_clear)
button_backspace = tk.Button(root, text="<<", padx=35, pady=20, font=("Arial", 18), command=button_backspace)

# Placing the buttons on the GUI
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_equal.grid(row=4, column=2, columnspan=2)

button_subtract.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5,column=2)
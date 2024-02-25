# Here I an creating a SIMPLE calculator using tkinter
              
# "*" imports all the functions, classes, constants into the current python file from the Tkinter module
from tkinter import *

admin = Tk()  # used to create a GUI window that will display the conrtents ('Tk()' is nuilt in)

admin.title("Simple Calculator") # creating a title of the window as "Simple-Calculator"


e = Entry(admin, width=30, borderwidth=5)  # "Entry" is a function used in python for displaying the text the user types
e.grid(row=1, column=1, columnspan=3)      # setting the position of the "Entry" bar


def click1(number):  # "def" is used to create and defining a function, returns the number we types when we will call this function later

    first_no = e.get()    # taking input of the 1st no.
    e.delete(0, END)      # deletes everything that are in the box
    e.insert(0, str(first_no) + str(number))   # inserts in the entry box

def clear():  # this function is used to clear everything in the calculator
    e.delete(0, END)

def add(): # defining "add()" function
    global first_number #  setting the variable as global 
    global calculation_of 
    first_number = e.get()
    calculation_of = "addition"
    e.delete(0, END)
    # ending the "add()"

def sub(): # defining "sub()" function
    global first_number
    global calculation_of
    first_number = e.get()
    calculation_of = "substraction"
    e.delete(0, END)
    # ending the "sub()" 

def mul(): # defining "mul()" function
    global first_number
    global calculation_of
    first_number = e.get()
    calculation_of = "multiplication"
    e.delete(0, END)
    # ending the "mul()"

def div(): # defining "div()" function
    global first_number
    global calculation_of
    first_number = e.get()
    calculation_of = "division"
    e.delete(0, END)
    # ending the "div()"

def equal(): # defining "equal()" function
    global first_number
    global calculation_of
    second_number = e.get() # takin input of the second number
    e.delete(0, END)
    # ending the "equal()"
    
    # using if statememt for directing the "equal()" function what operation to do whenever needed
    if calculation_of == "addition": # checks the condition wheather to perform addition or not
        e.insert(0, int(first_number) + int(second_number)) # adding the two numbers and displaying the output in the entry box
    
    if calculation_of == "substraction": # checks the condition wheather to perform subtraction or not
        # using if statement inside an if statement
        if first_number > second_number: # checks the condition 
            e.insert(0, int(first_number) - int(second_number)) # subtracting the first number friom the second and displaying the output in the entry box
        if first_number < second_number:
            e.insert(0, int(second_number) - int(first_number)) # subtracting the second number friom the first and displaying the output in the entry box

    if calculation_of == "division": # checks the condition wheather to perform division or not
        e.insert(0, int(first_number) / int(second_number)) # divides the first number from the other

    if calculation_of == "multiplication": # checks the condition wh eather to perform multiplication or not
        e.insert(0, int(first_number) * int(second_number)) # multiplies the first no with the other

  
# Creating the buttons to be clicked in the calculator
# here "Lambda" is used to call the function with the parameters
# "padx" and "pady" defines the padding of the button in both X and Y directions
button1 = Button(admin, text="1",padx=40, pady=20, command= lambda: click1(1)) 
button2 = Button(admin, text="2",padx=40, pady=20, command= lambda: click1(2))
button3 = Button(admin, text="3",padx=40, pady=20, command= lambda: click1(3))
button4 = Button(admin, text="4",padx=40, pady=20, command= lambda: click1(4))
button5 = Button(admin, text="5",padx=40, pady=20, command= lambda: click1(5))
button6 = Button(admin, text="6",padx=40, pady=20, command= lambda: click1(6))
button7 = Button(admin, text="7",padx=40, pady=20, command= lambda: click1(7))
button8 = Button(admin, text="8",padx=40, pady=20, command= lambda: click1(8))
button9 = Button(admin, text="9",padx=40, pady=20, command= lambda: click1(9))
button0 = Button(admin, text="0",padx=40, pady=20, command= lambda: click1(0))
# in the below buttons the function is directly called without parameters, so no "Lambda" is used
button_equal = Button(admin, text="=", width=13,padx=40, pady=20, command=equal)
button_add = Button(admin, text="+",padx=40, pady=20, command= add)
button_mul = Button(admin, text="x",padx=41, pady=20, command= mul)
button_div = Button(admin, text="÷",padx=40, pady=20, command= div)
button_sub = Button(admin, text="-",padx=42, pady=20, command= sub)
button_clear = Button(admin, text="Clear", width=13,padx=40, pady=20, command=clear)

# griding system is used to specify the position of the buttons by giving them a specific row and column 
button1.grid(row=2, column=1)
button2.grid(row=2, column=2)
button3.grid(row=2, column=3)
button4.grid(row=3, column=1)
button5.grid(row=3, column=2)
button6.grid(row=3, column=3)
button7.grid(row=4, column=1)
button8.grid(row=4, column=2)
button9.grid(row=4, column=3)
button0.grid(row=5, column=1)
button_equal.grid(row=5, column=2, columnspan=3)
button_add.grid(row=6, column=1)
button_clear.grid(row=6, column=2, columnspan=3)
button_sub.grid(row=7, column=1)
button_mul.grid(row=7, column=2)
button_div.grid(row=7, column=3)


# MAINLOOP is a loop that is used in many GUI based libraries in python that continously listens for the system user inputs, mouse clicks and other system inputs
admin.mainloop() # it is a must written loop so we cannot skip it

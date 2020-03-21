'''
A simple calculator using tkinter to perform simple operation
like addition,subtraction,multiplication,division.
'''
from tkinter import *

expression =''

# 'press' fuction to store the number durning input
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# 'clearbutton' function for clearing the input text when 'clear' button is clicked
def clearbutton():
    global expression
    expression = ""
    equation.set("")

# 'equaloption' function to perform operation when 'equal' button is clicked
def equaloption():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

root=Tk()

root.title("Calculator")#name of tkinter page
root.geometry('300x200')#size of tkinter page
equation=StringVar()
no_input=Entry(root,textvariable=equation)
no_input.grid(columnspan=4, ipadx=70)
equation.set("")
# button '1'
button1 = Button(root, text=' 1 ', fg='red', bg='yellow',command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)
# button '2'
button2 = Button(root, text=' 2 ', fg='red', bg='yellow',command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)
# button '3'
button3 = Button(root, text=' 3 ', fg='red', bg='yellow',command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)
# button '4'
button4 = Button(root, text=' 4 ', fg='red', bg='yellow',command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)
# button '5'
button5 = Button(root, text=' 5 ', fg='red', bg='yellow',command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)
# button '6'
button6 = Button(root, text=' 6 ', fg='red', bg='yellow',command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)
# button '7'
button7 = Button(root, text=' 7 ', fg='red', bg='yellow',command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)
# button '8'
button8 = Button(root, text=' 8 ', fg='red', bg='yellow',command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)
# button '9'
button9 = Button(root, text=' 9 ', fg='red', bg='yellow',command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)
# button '0'
button0 = Button(root, text=' 0 ', fg='red', bg='yellow',command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=0)
# button '+'
plus = Button(root, text=' + ', fg='red', bg='white',command=lambda: press("+"), height=1, width=7)
plus.grid(row=2, column=3)
# button '-'
minus = Button(root, text=' - ', fg='red', bg='white',command=lambda: press("-"), height=1, width=7)
minus.grid(row=3, column=3)
# button '*'
multiply = Button(root, text=' * ', fg='red', bg='white',command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4, column=3)
# button '/'
divide = Button(root, text=' / ', fg='red', bg='white',command=lambda: press("/"), height=1, width=7)
divide.grid(row=5, column=3)
# button '='
equal = Button(root, text=' = ', fg='black', bg='white',command=equaloption, height=1, width=7)
equal.grid(row=6, column=2)
# button 'Clear'
clear = Button(root, text='Clear', fg='black', bg='white',command=clearbutton, height=1, width=7)
clear.grid(row=6, column='1')

root.mainloop()
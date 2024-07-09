import tkinter as tk

root = tk.Tk()
root.title("My Python Calculator")
root.config(bg="grey")
root.geometry("600x400")
root.resizable(False, False)

label1 = tk.Label(root, text= "This is a calculator", bg="gray", font=('Helvetica,24'))
label1.pack(anchor=tk.W, expand=True, fill=tk.BOTH)

ex = tk.Label(root, text= "", bg="white", height=1)
ex.pack(anchor=tk.W, expand=True)

re = tk.Label(root, text= "", bg="white", height=1)
re.pack(anchor=tk.W, expand=True)

from tkinter import ttk;
frame = ttk.Frame(root, width=200, height=200, border=20, relief= "sunken")

number1 = 0
number2 = 0
operator = ""
result = 0

expression = ""
equalJustClick = False

def number_click(n):
    global operator
    global number1
    global number2
    global result
    global expression
    global ex
    global equalJustClick

    if equalJustClick == True:
        operator = ""
        number1 = 0
        number2 = 0
        result = 0
        expression = ""
        equalJustClick = False
    if operator == "":
        number1 = number1 * 10 + n
    else:
        number2 = number2 * 10 + n
    expression = expression + str(n)
    ex.configure(text = expression)
    re.configure(text = result)

def operator_click(s):
    global operator
    global expression
    global result
    global number1
    global number2
    global ex
    global equalJustClick

    equalJustClick = False
    if (operator == "/"):
        result = result / number2
    elif (operator == "*"):
        result = result * number2
    elif (operator == "-"):
        result = result - number2
    elif (operator == "+"):
        result = result + number2
    elif (operator == ""):
        result = number1
    else:
        result = result

    operator = s
    number2 = 0

    expression = expression + s
    ex.configure(text=expression)
    re.configure(text = str(result))

def equation_click():
    global operator
    global expression
    global result
    global number1
    global number2
    global ex
    global equalJustClick

    if operator == "":
        result = number1
    elif operator == "+":
        result = result + number2
        number2 == 0
    elif operator == "-":
        result = result - number2
        number2 == 0       
    elif operator == "*":
        result = result * number2
        number2 == 0
    elif operator == "/":
        if number2 != 0:
            result = result / number2
            number2 = 0
    else:
        result = result
    expression = expression + " = " + str(result) + ", " + str(result)
    ex.configure(text = expression)
    re.configure(text = result)
    equalJustClick = True

inverseButton = tk.Button(frame, text="1/x", bg="lightgray", font=('Helvetica', 18), width=2)
inverseButton.grid(row=0, column=0, sticky="W")

squareButton = tk.Button(frame, text="x2", bg="lightgray", font=('Helvetica', 18), width=2)
squareButton.grid(row=0, column=1, sticky="W")

sqrtButtun = tk.Button(frame, text="sqrt", bg="lightgray", font=('Helvetica', 18), width=2)
sqrtButtun.grid(row=0, column=2, sticky="W")

divisionButton = tk.Button(frame, text="/", bg="lightgray", font=('Helvetica', 18), width=2)
divisionButton.grid(row=0, column=3, sticky="W")
divisionButton.configure(command=lambda s="/": operator_click(s))

sevenButton = tk.Button(frame, text="7", bg="lightgray", font=('Helvetica', 18), width=2)
sevenButton.grid(row=1, column=0, sticky="W")
sevenButton.configure(command=lambda n=7: number_click(n))

eightButton = tk.Button(frame, text="8", bg="lightgray", font=('Helvetica', 18), width=2)
eightButton.grid(row=1, column=1, sticky="W")
eightButton.configure(command=lambda n=8: number_click(n))

nineButton = tk.Button(frame, text="9", bg="lightgray", font=('Helvetica', 18), width=2)
nineButton.grid(row=1, column=2, sticky="W")
nineButton.configure(command=lambda n=9: number_click(n))

multiplyButton = tk.Button(frame, text="x", bg="lightgray", font=('Helvetica', 18), width=2)
multiplyButton.grid(row=1, column=3, sticky="W")
multiplyButton.configure(command=lambda s="*": operator_click(s))

fourButton = tk.Button(frame, text="4", bg="lightgray", font=('Helvetica', 18), width=2)
fourButton.grid(row=2, column=0, sticky="W")
fourButton.configure(command=lambda n=4: number_click(n))

fiveButton = tk.Button(frame, text="5", bg="lightgray", font=('Helvetica', 18), width=2)
fiveButton.grid(row=2, column=1, sticky="W")
fiveButton.configure(command=lambda n=5: number_click(n))

sixButton = tk.Button(frame, text="6", bg="lightgray", font=('Helvetica', 18), width=2)
sixButton.grid(row=2, column=2, sticky="W")
sixButton.configure(command=lambda n=6: number_click(n))

minusButton = tk.Button(frame, text="-", bg="lightgray", font=('Helvetica', 18), width=2)
minusButton.grid(row=2, column=3, sticky="W")
minusButton.configure(command=lambda s="-": operator_click(s))

oneButton = tk.Button(frame, text="1", bg="lightgray", font=('Helvetica', 18), width=2)
oneButton.grid(row=3, column=0, sticky="W")
oneButton.configure(command=lambda n=1: number_click(n))

twoButton = tk.Button(frame, text="2", bg="lightgray", font=('Helvetica', 18), width=2)
twoButton.grid(row=3, column=1, sticky="W")
twoButton.configure(command=lambda n=2: number_click(n))

threeButton = tk.Button(frame, text="3", bg="lightgray", font=('Helvetica', 18), width=2)
threeButton.grid(row=3, column=2, sticky="W")
threeButton.configure(command=lambda n=3: number_click(n))

plusButton = tk.Button(frame, text="+", bg="lightgray", font=('Helvetica', 18), width=2)
plusButton.grid(row=3, column=3, sticky="W")
plusButton.configure(command=lambda s="+": operator_click(s))

pmButton = tk.Button(frame, text="+/-", bg="lightgray", font=('Helvetica', 18), width=2)
pmButton.grid(row=4, column=0, sticky="W")

zeroButton = tk.Button(frame, text="0", bg="lightgray", font=('Helvetica', 18), width=2)
zeroButton.grid(row=4, column=1, sticky="W")
zeroButton.configure(command=lambda n=0: number_click(n))

dotButton = tk.Button(frame, text=".", bg="lightgray", font=('Helvetica', 18), width=2)
dotButton.grid(row=4, column=2, sticky="W")

equationButton = tk.Button(frame, text="=", bg="lightgray", font=('Helvetica', 18), width=2)
equationButton.grid(row=4, column=3, sticky="W")
equationButton.configure(command=lambda : equation_click())

frame.pack(anchor = tk.W, expand=True, fill=tk.BOTH)
root.mainloop()
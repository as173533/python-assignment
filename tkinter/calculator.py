import tkinter as tk
import math

# Window
window = tk.Tk()
window.title("Standard Calculator")
window.geometry("340x520")
window.resizable(False, False)
window.configure(bg="#1e1e1e")

expression = ""

# Display
e = tk.Entry(window, font=("Arial", 22), bd=0, bg="#2d2d2d", fg="white", justify="right")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=15, sticky="nsew")

# Functions
def press(value):
    global expression
    expression += str(value)
    e.delete(0, tk.END)
    e.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    e.delete(0, tk.END)

def equal():
    global expression
    try:
        result = str(eval(expression))
        e.delete(0, tk.END)
        e.insert(tk.END, result)
        expression = result
    except:
        e.delete(0, tk.END)
        e.insert(tk.END, "Error")
        expression = ""

def percent():
    global expression
    try:
        result = str(eval(expression) / 100)
        e.delete(0, tk.END)
        e.insert(tk.END, result)
        expression = result
    except:
        e.insert(tk.END, "Error")

def sqrt():
    global expression
    try:
        result = str(math.sqrt(float(expression)))
        e.delete(0, tk.END)
        e.insert(tk.END, result)
        expression = result
    except:
        e.delete(0, tk.END)
        e.insert(tk.END, "Error")
        expression = ""
def backspace():
    global expression
    expression = expression[:-1]   # remove last character
    e.delete(0, tk.END)
    e.insert(tk.END, expression)

# Button style
btn_style = {
    "font": ("Arial", 14),
    "bd": 0,
    "fg": "white",
    "width": 5,
    "height": 2
}

# Buttons layout
buttons = [
    ("C", 1, 0), ("⌫", 1, 1), ("%", 1, 2), ("√", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3)
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        action = equal
        bg = "#4CAF50"
    elif text == "C":
        action = clear
        bg = "#f44336"
    elif text == "%":
        action = percent
        bg = "#9C27B0"
    elif text == "√":
        action = sqrt
        bg = "#009688"
    elif text in "+-*/":
        action = lambda x=text: press(x)
        bg = "#ff9800"
    elif text == "⌫":
        action = backspace
        bg = "#607D8B"
    else:
        action = lambda x=text: press(x)
        bg = "#3a3a3a"

    tk.Button(window, text=text, command=action, bg=bg, **btn_style)\
        .grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Grid resize
for i in range(6):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

window.mainloop()
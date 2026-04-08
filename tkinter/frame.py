import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title("Frame Color")
window.geometry("400x300")

my_frame = ttk.Frame(window)
my_frame.pack(side="left",fill="both",expand=True)

label1 = tk.Label(window,text="Hello World", bg="red")
label1.pack(side="top", fill="both", expand=True)

label2 = tk.Label(window,text="How are you?", bg="blue")
label2.pack(side="top", fill="both", expand=True)

label3 = tk.Label(window,text="Have a nice day", bg="green")
label3.pack(side="top", fill="both", expand=True)

window.mainloop()
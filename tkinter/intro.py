import tkinter as tk
import tkinter.font as tfont
from tkinter.constants import YES
from tkinter import ttk

window = tk.Tk()
window.title("INTRO")
# window.geometry("500x500")
window.minsize(300,500)
# customfont = tfont.Font(family="Times New Roman",size=20,weight="bold",slant="italic",underline=0)

#LABEL
label = ttk.Label(window,text="Hello World", padding=5)
label.pack()

label.config(text="Thank you Again")
# label.config(font=("Courier New",20))

#INPUT
user_input = ttk.Entry(width=35)
# user_input = ttk.Entry(width=35,show="*")
user_input.pack()


counter = 0
def function_button():
    text = user_input.get()
    global counter
    counter += 1
    label['text'] = f"{text} is {counter} times"
#BUTTON
button = ttk.Button(window,text="Click Me",command=function_button)
button.pack()

quiet_button = ttk.Button(window,text="Quit",command=window.destroy)
quiet_button.pack()

separator = ttk.Separator(window,orient="horizontal")
separator.pack(fill="x",)

#TEXT BOX
text = tk.Text(window, height=3,width=35)
text.pack()
text.focus()
text.insert(1.0,"Hello World")

text_data = text.get("1.0","end")

def text_function():
    global text_data
    text_data = text.get("1.0","end")
    print(text_data)

text_button = ttk.Button(window,text="Get text",command=text_function)
text_button.pack()



# text["state"] = "disabled"
#
# def enable_text():
#     text["state"] = "normal"
#     enable_button["text"] = "Disabled Text"
#     enable_button["command"] = disabled_text
#
# def disabled_text():
#     text["state"] = "disabled"
#     enable_button["text"] = "Enable Text"
#     enable_button["command"] = enable_text
#
# enable_button = ttk.Button(window,text="Enable text",command=enable_text)
# enable_button.pack()

#CHECK BUTTON

check_option = tk.BooleanVar()

def check_option_function():
    print(check_option.get())

check_button = ttk.Checkbutton(window,text="Agree Terms & Conditions", variable= check_option
                               ,command=check_option_function)
check_button.pack()

#RADIO BUTTON
radio_value = tk.StringVar()


def get_radio_value_function():
    print(radio_value.get())

option1 = ttk.Radiobutton(window,text="Male",variable= radio_value, value="male", command=get_radio_value_function)
option1.pack()

option2 = ttk.Radiobutton(window,text="Female",variable= radio_value, value="female", command=get_radio_value_function)
option2.pack()

#COMBO BOX
selected_country = tk.StringVar()

countries = ttk.Combobox(window,textvariable=selected_country, values=["India","China","Japan"])
countries["state"] = "readonly"
countries.pack()

def display_country_function(event):
    print(f"Selected Country: {selected_country.get()}")

countries.bind("<<ComboboxSelected>>",display_country_function)

#LISTBOX
food_items = ("Pizza","Burger","FUCHKA","JILEPI")
selected_food = tk.StringVar(value=food_items)

food_list = tk.Listbox(listvariable=selected_food,height=3, selectmode="extended")
food_list.pack()

def display_food_function(event):
    food_indices = food_list.curselection()
    for food_index in food_indices:
        print(food_list.get(food_index))


food_list.bind("<<ListboxSelect>>",display_food_function)

#SPINBOX
def get_spinbox_function():
    print(spin_box.get())

spinboxcounter = tk.IntVar(value=0)
# spin_box = ttk.Spinbox(from_=0,to=20,textvariable=spinboxcounter, wrap=True, command=get_spinbox_function)
# spin_box = ttk.Spinbox(values=(10,15,202,203),textvariable=spinboxcounter, wrap=True, command=get_spinbox_function)
spin_box = ttk.Spinbox(values=tuple(range(10,200,5)),textvariable=spinboxcounter, wrap=True, command=get_spinbox_function)
spin_box.pack()



window.mainloop()


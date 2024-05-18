#import libraries
from tkinter import Tk, Frame, Label, LabelFrame, Text, Entry, Button, Checkbutton, IntVar, StringVar, DISABLED, NORMAL, END, RIDGE, TOP, LEFT, Y, RIGHT, W, BOTTOM
from tkinter import filedialog, messagebox
import random
import time
import secrets

#function to save the receipt to a file
def save_receipt():
    file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    receipt_details = receipt_text.get(1.0, END)
    file.write(receipt_details)
    file.close()
    messagebox.showinfo('Information:', message='Receipt stored successfully')

#function to clear all input fields and reset variables
def clear_all():
    receipt_text.delete(1.0, END)
    reset_text_vars()
    reset_state()
    reset_cost_entries()

def reset_text_vars():
    #resetting text variables
    txtYuzu.set("0")
    txtMintGinger.set("0")
    txtChocolate.set("0")
    txtMatchaLatte.set("0")
    txtEspresso.set("0")
    txtDoubleEspresso.set("0")

def reset_state():
    #disabling text entries
    textYuzu.config(state=DISABLED)
    textMintGinger.config(state=DISABLED)
    textChocolate.config(state=DISABLED)
    textMatchaLatte.config(state=DISABLED)
    textEspresso.config(state=DISABLED)
    textDoubleEspresso.config(state=DISABLED)

    #resetting checkbutton variables
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)

def reset_cost_entries():
    #resetting cost variables
    global varTeaCost, varNoncoffeeCost, varCoffeeCost, varSubtotal, varIVA, varTotal
    varTeaCost = 0
    varNoncoffeeCost = 0
    varCoffeeCost = 0
    varSubtotal = 0
    varIVA = 0
    varTotal = 0

    #updating the entries
    update_cost_entry(checkboxTeaCost, varTeaCost)
    update_cost_entry(checkboxNoncoffeeCost, varNoncoffeeCost)
    update_cost_entry(checkboxCoffeeCost, varCoffeeCost)
    update_cost_entry(checkboxSubtotal, varSubtotal)
    update_cost_entry(checkboxIVA, varIVA)
    update_cost_entry(checkboxTotal, varTotal)

def update_cost_entry(entry, value):
    entry.config(state=NORMAL)
    entry.delete(0, END)
    entry.insert(0, value)
    entry.config(state=DISABLED)

#function to create the receipt content
def create_receipt():
    receipt_text.delete(1.0, END)
    receipt_number = f"Num{secrets.randbelow(1000)+1}"
    date = time.strftime('%d-%m-%y')
    
    receipt_text.insert(END, f'Bill-> {receipt_number}\t\t\t Date: {date}\n')
    receipt_text.insert(END, '*************************************************************\n')
    receipt_text.insert(END, 'Totals \t\t\t\t Quantities: \n')
    receipt_text.insert(END, '*************************************************************\n')
    receipt_text.insert(END, f'Total in Tea ----------------------------------------> €{varTeaCost}\n')
    receipt_text.insert(END, f'Total in Non-Coffee -----------------------------> €{varNoncoffeeCost}\n')
    receipt_text.insert(END, f'Total in Coffee ------------------------------------> €{varCoffeeCost}\n')
    receipt_text.insert(END, f'Subtotal ---------------------------------------------> €{subtotal}\n')
    receipt_text.insert(END, f'IVA ----------------------------------------------------> €{iva}\n')
    receipt_text.insert(END, '*************************************************************\n\n')
    receipt_text.insert(END, f'FINAL TOTAL -------------------------------------> €{total}\n')

#function to calculate the grand total
def calculate_grand_total():
    calculate_tea_cost()
    calculate_noncoffee_cost()
    calculate_coffee_cost()
    calculate_subtotal()
    calculate_iva()
    calculate_total()

#function to calculate tea cost
def calculate_tea_cost():
    global varTeaCost
    yuzu_qty = int(textYuzu.get())
    mint_ginger_qty = int(textMintGinger.get())
    varTeaCost = round((yuzu_qty * 3.5) + (mint_ginger_qty * 3.5), 2)
    update_cost_entry(checkboxTeaCost, varTeaCost)

#function to calculate non-coffee cost
def calculate_noncoffee_cost():
    global varNoncoffeeCost
    chocolate_qty = int(textChocolate.get())
    matcha_latte_qty = int(textMatchaLatte.get())
    varNoncoffeeCost = round((chocolate_qty * 4) + (matcha_latte_qty * 4.5), 2)
    update_cost_entry(checkboxNoncoffeeCost, varNoncoffeeCost)

#function to calculate coffee cost
def calculate_coffee_cost():
    global varCoffeeCost
    espresso_qty = int(textEspresso.get())
    double_espresso_qty = int(textDoubleEspresso.get())
    varCoffeeCost = round((espresso_qty * 2) + (double_espresso_qty * 3), 2)
    update_cost_entry(checkboxCoffeeCost, varCoffeeCost)

#function to calculate subtotal
def calculate_subtotal():
    global subtotal
    subtotal = round(varTeaCost + varNoncoffeeCost + varCoffeeCost, 2)
    update_cost_entry(checkboxSubtotal, subtotal)

#function to calculate IVA
def calculate_iva():
    global iva
    iva = round(subtotal * 0.16, 2)
    update_cost_entry(checkboxIVA, iva)

#function to calculate total
def calculate_total():
    global total
    total = round(subtotal + iva, 2)
    update_cost_entry(checkboxTotal, total)

#functions to enable and disable checkboxes and text entries
#tea
def toggle_yuzu():
    toggle_entry(var1, textYuzu, txtYuzu)

def toggle_mint_ginger():
    toggle_entry(var2, textMintGinger, txtMintGinger)

#non-coffee
def toggle_chocolate():
    toggle_entry(var3, textChocolate, txtChocolate)

def toggle_matcha_latte():
    toggle_entry(var4, textMatchaLatte, txtMatchaLatte)

#coffee
def toggle_espresso():
    toggle_entry(var5, textEspresso, txtEspresso)

def toggle_double_espresso():
    toggle_entry(var6, textDoubleEspresso, txtDoubleEspresso)

def toggle_entry(var, text_widget, text_var):
    if var.get() == 1:
        text_widget.config(state=NORMAL)
        text_widget.delete(0, END)
        text_widget.focus()
    else:
        text_widget.config(state=DISABLED)
        text_var.set("0")

#design of the main screen
screen = Tk()
screen.title("Our Coffee System")
screen.geometry("1300x720")
screen.resizable(0, 0)
screen.config(bg="darkblue")

#setting up the fonts for the titles
Title = ("arial black", 25)
Subtitle = ("consolas", 14)

#main title frame
upper_frame = Frame(screen, bd=12, relief=RIDGE, bg="blue")
upper_frame.pack(side=TOP)

#main title
main_title = Label(upper_frame, text="Our Coffee System", font=Title, fg="white", bg="blue", width=53)
main_title.grid(row=0, column=0)

#secondary frames
menu_frame = Frame(screen, bd=10, relief=RIDGE, bg="blue")
menu_frame.pack(side=LEFT, fill=Y)

cost_frame = Frame(menu_frame, bd=2, relief=RIDGE, bg="blue")
cost_frame.pack(side=BOTTOM)

tea_frame = LabelFrame(menu_frame, text="Tea", bd=5, font=Subtitle, relief=RIDGE, bg="lightgray")
tea_frame.pack(side=LEFT, fill=Y)

noncoffee_frame = LabelFrame(menu_frame, text="Non-Coffee", bd=5, font=Subtitle, relief=RIDGE, bg="lightgray")
noncoffee_frame.pack(side=LEFT, fill=Y)

coffee_frame = LabelFrame(menu_frame, text="Coffee", bd=5, font=Subtitle, relief=RIDGE, bg="lightgray")
coffee_frame.pack(side=LEFT, fill=Y)

#right frames
right_frame = Frame(screen, bd=10, relief=RIDGE, bg="blue")
right_frame.pack(side=RIGHT)

receipt_frame = Frame(right_frame, bd=5, relief=RIDGE, bg="blue")
receipt_frame.pack()

button_frame = Frame(right_frame, bd=5, relief=RIDGE, bg="blue")
button_frame.pack()

#receipt text box
receipt_text = Text(receipt_frame, font=("arial", 12, "bold"), bd=3, width=42, height=17)
receipt_text.grid(row=0, column=0)

#variables for checkbuttons
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()

#variables for text entries
txtYuzu = StringVar(value="0")
txtMintGinger = StringVar(value="0")
txtChocolate = StringVar(value="0")
txtMatchaLatte = StringVar(value="0")
txtEspresso = StringVar(value="0")
txtDoubleEspresso = StringVar(value="0")

#tea section widgets
checkboxYuzu = Checkbutton(tea_frame, text="Yuzu Tea", font=Subtitle, onvalue=1, offvalue=0, variable=var1, command=toggle_yuzu)
checkboxYuzu.grid(row=0, column=0, sticky=W)

textYuzu = Entry(tea_frame, font=Subtitle, bd=8, width=6, state=DISABLED, textvariable=txtYuzu)
textYuzu.grid(row=0, column=1)

checkboxMintGinger = Checkbutton(tea_frame, text="Mint Ginger Tea", font=Subtitle, onvalue=1, offvalue=0, variable=var2, command=toggle_mint_ginger)
checkboxMintGinger.grid(row=1, column=0, sticky=W)

textMintGinger = Entry(tea_frame, font=Subtitle, bd=8, width=6, state=DISABLED, textvariable=txtMintGinger)
textMintGinger.grid(row=1, column=1)

#non-coffee section widgets
checkboxChocolate = Checkbutton(noncoffee_frame, text="Hot Chocolate", font=Subtitle, onvalue=1, offvalue=0, variable=var3, command=toggle_chocolate)
checkboxChocolate.grid(row=0, column=0, sticky=W)

textChocolate = Entry(noncoffee_frame, font=Subtitle, bd=8, width=6, state=DISABLED, textvariable=txtChocolate)
textChocolate.grid(row=0, column=1)

checkboxMatchaLatte = Checkbutton(noncoffee_frame, text="Matcha Latte", font=Subtitle, onvalue=1, offvalue=0, variable=var4, command=toggle_matcha_latte)
checkboxMatchaLatte.grid(row=1, column=0, sticky=W)

textMatchaLatte = Entry(noncoffee_frame, font=Subtitle, bd=8, width=6, state=DISABLED, textvariable=txtMatchaLatte)
textMatchaLatte.grid(row=1, column=1)

#coffee section widgets
checkboxEspresso = Checkbutton(coffee_frame, text="Espresso", font=Subtitle, onvalue=1, offvalue=0, variable=var5, command=toggle_espresso)
checkboxEspresso.grid(row=0, column=0, sticky=W)

textEspresso = Entry(coffee_frame, font=Subtitle, bd=8, width=6, state=DISABLED, textvariable=txtEspresso)
textEspresso.grid(row=0, column=1)

checkboxDoubleEspresso = Checkbutton(coffee_frame, text="Double Espresso", font=Subtitle, onvalue=1, offvalue=0, variable=var6, command=toggle_double_espresso)
checkboxDoubleEspresso.grid(row=1, column=0, sticky=W)

textDoubleEspresso = Entry(coffee_frame, font=Subtitle, bd=8, width=6, state=DISABLED, textvariable=txtDoubleEspresso)
textDoubleEspresso.grid(row=1, column=1)

#total section widgets
varTeaCost = 0
varNoncoffeeCost = 0
varCoffeeCost = 0
subtotal = 0
iva = 0
total = 0

checkboxTeaCost = Entry(cost_frame, font=("arial", 12, "bold"), bd=8, width=18, state=DISABLED)
checkboxTeaCost.grid(row=0, column=1, padx=41)

checkboxNoncoffeeCost = Entry(cost_frame, font=("arial", 12, "bold"), bd=8, width=18, state=DISABLED)
checkboxNoncoffeeCost.grid(row=1, column=1, padx=41)

checkboxCoffeeCost = Entry(cost_frame, font=("arial", 12, "bold"), bd=8, width=18, state=DISABLED)
checkboxCoffeeCost.grid(row=2, column=1, padx=41)

checkboxSubtotal = Entry(cost_frame, font=("arial", 12, "bold"), bd=8, width=18, state=DISABLED)
checkboxSubtotal.grid(row=3, column=1, padx=41)

checkboxIVA = Entry(cost_frame, font=("arial", 12, "bold"), bd=8, width=18, state=DISABLED)
checkboxIVA.grid(row=4, column=1, padx=41)

checkboxTotal = Entry(cost_frame, font=("arial", 12, "bold"), bd=8, width=18, state=DISABLED)
checkboxTotal.grid(row=5, column=1, padx=41)

#labels for totals
total_labels = [
    ("Total in Tea", 0), 
    ("Total in Non-Coffee", 1), 
    ("Total in Coffee", 2), 
    ("Subtotal", 3), 
    ("IVA", 4), 
    ("Total", 5)
]

for text, row in total_labels:
    Label(cost_frame, font=("arial", 12, "bold"), text=text, bg="blue", fg="white").grid(row=row, column=0)

#buttons
Button(button_frame, text='Total', font=Subtitle, fg='black', bg='green', bd=5, padx=5, command=calculate_grand_total).grid(row=0, column=0)
Button(button_frame, text='Receipt', font=Subtitle, fg='black', bg='green', bd=5, padx=5, command=create_receipt).grid(row=0, column=1)
Button(button_frame, text='Save', font=Subtitle, fg='black', bg='green', bd=5, padx=5, command=save_receipt).grid(row=0, column=2)
Button(button_frame, text='Reset', font=Subtitle, fg='black', bg='green', bd=5, padx=5, command=clear_all).grid(row=0, column=3)
Button(button_frame, text='Exit', font=Subtitle, fg='black', bg='green', bd=5, padx=5, command=screen.destroy).grid(row=0, column=4)

#main loop
screen.mainloop()

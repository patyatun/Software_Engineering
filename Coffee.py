#import libraries
from tkinter import *
from tkinter import filedialog, messagebox
import random
import time

#function to save the receipt 
def save():
    url= filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    receiptDetails= receiptText.get(1.0, END)
    url.write(receiptDetails)
    url.close()
    messagebox.showinfo('Information:', message='Receipt stored successfully')

#function to clear all the values
def delete():
    receiptText.delete(1.0, END)
    #tea
    txtYuzu.set("0")
    txtHintGinger.set("0")
    txtJujubeGoji.set("0")
    txtLycheeOolong.set("0")
    txtGuavaJasmin.set("0")
    txtBlackLemon.set("0")
    txtMatchaLemon.set("0")
    #non-coffe
    txtChocolate.set("0")
    txtMatchaLatte.set("0")
    txtUbeOatLatte.set("0")
    #coffee
    txtEspresso.set("0")
    txtDoubleEspresso.set("0")
    txtAmericano.set("0")
    txtCapuccino.set("0")
    txtFlatWhite.set("0")
    txtLatte.set("0")
    txtMocha.set("0")
    txtBiscoffLatte.set("0")
    txtDalgonaLatte.set("0")
    txtBlackSesamLatte.set("0")
    txtInjeolmiOatLatte.set("0")
    txtPistacchioOatLatte.set("0")

    textYuzu.config(state= DISABLED)
    textHintGinger.config(state= DISABLED)
    textJujubeGoji.config(state= DISABLED)
    textLycheeOolong.config(state= DISABLED)
    textGuavaJasmin.config(state= DISABLED)
    textBlackLemon.config(state= DISABLED)
    textMatchaLemon.config(state= DISABLED)

    textChocolate.config(state= DISABLED)
    textMatchaLatte.config(state= DISABLED)
    textUbeOatLatte.config(state= DISABLED)

    textEspresso.config(state= DISABLED)
    textDoubleEspresso.config(state= DISABLED)
    textAmericano.config(state= DISABLED)
    textCapuccino.config(state= DISABLED)
    textFlatWhite.config(state= DISABLED)
    textLatte.config(state= DISABLED)
    textMocha.config(state= DISABLED)
    textBiscoffLatte.config(state= DISABLED)
    textDalgonaLatte.config(state= DISABLED)
    textBlackSesamLatte.config(state= DISABLED)
    textInjeolmiOatLatte.config(state= DISABLED)
    textPistacchioOatLatte.config(state= DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)

    global varTeaCost, varNoncoffeCost, varCoffeeCost, varSubtotal, varIVA, varTotal
    varTeaCost= 0
    varNoncoffeCost= 0
    varCoffeeCost= 0
    varSubtotal= 0
    varIVA= 0
    varTotal= 0

    checkboxTeaCost.config(state= NORMAL)
    checkboxTeaCost.delete(0, END)
    checkboxTeaCost.insert(0, varTeaCost)
    checkboxTeaCost.config(state= DISABLED)

    checkboxNoncoffeeCost.config(state= NORMAL)
    checkboxNoncoffeeCost.delete(0, END)
    checkboxNoncoffeeCost.insert(0, varNoncoffeCost)
    checkboxNoncoffeeCost.config(state= DISABLED)

    checkboxCoffeeCost.config(state= NORMAL)
    checkboxCoffeeCost.delete(0, END)
    checkboxCoffeeCost.insert(0, varCoffeeCost)
    checkboxCoffeeCost.config(state= DISABLED)

    checkboxSubtotal.config(state= NORMAL)
    checkboxSubtotal.delete(0, END)
    checkboxSubtotal.insert(0, varSubtotal)
    checkboxSubtotal.config(state= DISABLED)

    checkboxIVA.config(state= NORMAL)
    checkboxIVA.delete(0, END)
    checkboxIVA.insert(0, varIVA)
    checkboxIVA.config(state= DISABLED)

    checkboxTotal.config(state= NORMAL)
    checkboxTotal.delete(0, END)
    checkboxTotal.insert(0, varTotal)
    checkboxTotal.config(state= DISABLED)

#function to create the receipt
def receipt():
    receiptText.delete(1.0, END)
    x= random.randint(1, 1000)
    receiptNum= "Num"+str(x)
    date= time.strftime('%d-%m-%y')
    receiptText.insert(END, 'Bill->' + receiptNum + '\t\t\t\t\t Date:' + date + '\n')
    receiptText.insert(END, '************************************************************************************\n')
    receiptText.insert(END, 'Totals \t\t\t\t\t Quantities: \n')
    receiptText.insert(END, '************************************************************************************\n')
    receiptText.insert(END, 'Total in Tea ---------------------------------------------------> €' + str(varTeaCost) + '\n')
    receiptText.insert(END, 'Total in Non-Coffee ----------------------------------------> €' + str(varNoncoffeCost) + '\n')
    receiptText.insert(END, 'Total in Coffee -----------------------------------------------> €' + str(varCoffeeCost) + '\n')
    receiptText.insert(END, 'Subtotal --------------------------------------------------------> €' + str(subtotal) + '\n')
    receiptText.insert(END, 'IVA ---------------------------------------------------------------> €' + str(iva) + '\n')
    receiptText.insert(END, '************************************************************************************\n\n')
    receiptText.insert(END, 'FINAL TOTAL ------------------------------------------------> €' + str(total) + '\n')


#functions for totals
#funtion for the final total
def grantotal():
    global varTeaCost, varNoncoffeCost, varCoffeeCost, subtotal, iva, total
    #tea values
    t_Yuzu= int(textYuzu.get())
    t_HintGinger= int(textHintGinger.get())
    t_JujubeGoji= int(textJujubeGoji.get())
    t_LycheeOolong= int(textLycheeOolong.get())
    t_GuavaJasmin= int(textGuavaJasmin.get())
    t_BlackLemon= int(textBlackLemon.get())
    t_MatchaLemon= int(textMatchaLemon.get())
    varTeaCost= (t_Yuzu * 3.5) + (t_HintGinger * 3.5) + (t_JujubeGoji * 3.8) + (t_LycheeOolong * 4.5) + (t_GuavaJasmin * 4.5) + (t_BlackLemon * 4.5) + \
        (t_MatchaLemon * 4.5)
    checkboxTeaCost.config(state= NORMAL)
    checkboxTeaCost.delete(0, END)
    checkboxTeaCost.insert(0, varTeaCost)
    checkboxTeaCost.config(state= DISABLED)

    #non-coffee values
    t_Chocolate= int(textChocolate.get())
    t_MatchaLatte= int(textMatchaLatte.get())
    t_UbeOatLatte= int(textUbeOatLatte.get())
    varNoncoffeCost= (t_Chocolate * 4) + (t_MatchaLatte * 4.5) + (t_UbeOatLatte * 4.8)
    checkboxNoncoffeeCost.config(state= NORMAL)
    checkboxNoncoffeeCost.delete(0, END)
    checkboxNoncoffeeCost.insert(0, varNoncoffeCost)
    checkboxNoncoffeeCost.config(state= DISABLED)

    #coffee values
    t_Espresso= int(textEspresso.get())
    t_DoubleEspresso= int(textDoubleEspresso.get())
    t_Americano= int(textAmericano.get())
    t_Capuccino= int(textCapuccino.get())
    t_FlatWhite= int(textFlatWhite.get())
    t_Latte= int(textLatte.get())
    t_Mocha= int(textMocha.get())
    t_BiscoffLatte= int(textBiscoffLatte.get())
    t_DalgonaLatte= int(textDalgonaLatte.get())
    t_BlackSesamLatte= int(textBlackSesamLatte.get())
    t_InjeolmiOatLatte= int(textInjeolmiOatLatte.get())
    t_PistacchioOatLatte= int(textPistacchioOatLatte.get())
    varCoffeeCost= (t_Espresso * 2) + (t_DoubleEspresso * 3) + (t_Americano * 2.5) + (t_Capuccino * 3.5) + (t_FlatWhite * 4) + (t_Latte * 3.8) + \
        (t_Mocha * 4.5) + (t_BiscoffLatte * 4.5) + (t_DalgonaLatte * 4.9) + (t_BlackSesamLatte * 4.8) + (t_InjeolmiOatLatte * 5.2) + (t_PistacchioOatLatte * 5.4)
    checkboxCoffeeCost.config(state= NORMAL)
    checkboxCoffeeCost.delete(0, END)
    checkboxCoffeeCost.insert(0, varCoffeeCost)
    checkboxCoffeeCost.config(state= DISABLED)

    subtotal= varTeaCost + varNoncoffeCost + varCoffeeCost
    checkboxSubtotal.config(state= NORMAL)
    checkboxSubtotal.delete(0, END)
    checkboxSubtotal.insert(0, subtotal)
    checkboxSubtotal.config(state= DISABLED)

    iva= float(checkboxSubtotal.get())*0.12
    checkboxIVA.config(state= NORMAL)
    checkboxIVA.delete(0, END)
    checkboxIVA.insert(0, iva)
    checkboxIVA.config(state= DISABLED)

    total= subtotal + iva
    checkboxTotal.config(state= NORMAL)
    checkboxTotal.delete(0, END)
    checkboxTotal.insert(0, total)
    checkboxTotal.config(state= DISABLED)

#functions to enable and disable checkboxes
#tea
def yuzu():
    if var1.get()==1:
        textYuzu.config(state= NORMAL)
        textYuzu.delete(0, END)
        textYuzu.focus()
    else:
        textYuzu.config(state= DISABLED)
        txtYuzu.set("0")

def hintGinger():
    if var2.get()==1:
        textHintGinger.config(state= NORMAL)
        textHintGinger.delete(0, END)
        textHintGinger.focus()
    else:
        textHintGinger.config(state= DISABLED)
        txtHintGinger.set("0")

def jujubeGoji():
    if var3.get()==1:
        textJujubeGoji.config(state= NORMAL)
        textJujubeGoji.delete(0, END)
        textJujubeGoji.focus()
    else:
        textJujubeGoji.config(state= DISABLED)
        txtJujubeGoji.set("0")

def lycheeOolong():
    if var4.get()==1:
        textLycheeOolong.config(state= NORMAL)
        textLycheeOolong.delete(0, END)
        textLycheeOolong.focus()
    else:
        textLycheeOolong.config(state= DISABLED)
        txtLycheeOolong.set("0")

def guavaJasmin():
    if var5.get()==1:
        textGuavaJasmin.config(state= NORMAL)
        textGuavaJasmin.delete(0, END)
        textGuavaJasmin.focus()
    else:
        textGuavaJasmin.config(state= DISABLED)
        txtGuavaJasmin.set("0")

def blackLemon():
    if var6.get()==1:
        textBlackLemon.config(state= NORMAL)
        textBlackLemon.delete(0, END)
        textBlackLemon.focus()
    else:
        textBlackLemon.config(state= DISABLED)
        txtBlackLemon.set("0")

def matchaLemon():
    if var7.get()==1:
        textMatchaLemon.config(state= NORMAL)
        textMatchaLemon.delete(0, END)
        textMatchaLemon.focus()
    else:
        textMatchaLemon.config(state= DISABLED)
        txtMatchaLemon.set("0")

#non-coffee
def chocolate():
    if var8.get()==1:
        textChocolate.config(state= NORMAL)
        textChocolate.delete(0, END)
        textChocolate.focus()
    else:
        textChocolate.config(state= DISABLED)
        txtChocolate.set("0")

def matchaLatte():
    if var9.get()==1:
        textMatchaLatte.config(state= NORMAL)
        textMatchaLatte.delete(0, END)
        textMatchaLatte.focus()
    else:
        textMatchaLatte.config(state= DISABLED)
        txtMatchaLatte.set("0")

def ubeOatLatte():
    if var10.get()==1:
        textUbeOatLatte.config(state= NORMAL)
        textUbeOatLatte.delete(0, END)
        textUbeOatLatte.focus()
    else:
        textUbeOatLatte.config(state= DISABLED)
        txtUbeOatLatte.set("0")

#coffee
def espresso():
    if var11.get()==1:
        textEspresso.config(state= NORMAL)
        textEspresso.delete(0, END)
        textEspresso.focus()
    else:
        textEspresso.config(state= DISABLED)
        txtEspresso.set("0")

def doubleEspresso():
    if var12.get()==1:
        textDoubleEspresso.config(state= NORMAL)
        textDoubleEspresso.delete(0, END)
        textDoubleEspresso.focus()
    else:
        textDoubleEspresso.config(state= DISABLED)
        txtDoubleEspresso.set("0")

def americano():
    if var13.get()==1:
        textAmericano.config(state= NORMAL)
        textAmericano.delete(0, END)
        textAmericano.focus()
    else:
        textAmericano.config(state= DISABLED)
        txtAmericano.set("0")

def capuccino():
    if var14.get()==1:
        textCapuccino.config(state= NORMAL)
        textCapuccino.delete(0, END)
        textCapuccino.focus()
    else:
        textCapuccino.config(state= DISABLED)
        txtCapuccino.set("0")

def flatWhite():
    if var15.get()==1:
        textFlatWhite.config(state= NORMAL)
        textFlatWhite.delete(0, END)
        textFlatWhite.focus()
    else:
        textFlatWhite.config(state= DISABLED)
        txtFlatWhite.set("0")

def latte():
    if var16.get()==1:
        textLatte.config(state= NORMAL)
        textLatte.delete(0, END)
        textLatte.focus()
    else:
        textLatte.config(state= DISABLED)
        txtLatte.set("0")

def mocha():
    if var17.get()==1:
        textMocha.config(state= NORMAL)
        textMocha.delete(0, END)
        textMocha.focus()
    else:
        textMocha.config(state= DISABLED)
        txtMocha.set("0")

def biscoffLatte():
    if var18.get()==1:
        textBiscoffLatte.config(state= NORMAL)
        textBiscoffLatte.delete(0, END)
        textBiscoffLatte.focus()
    else:
        textBiscoffLatte.config(state= DISABLED)
        txtBiscoffLatte.set("0")

def dalgonaLatte():
    if var19.get()==1:
        textDalgonaLatte.config(state= NORMAL)
        textDalgonaLatte.delete(0, END)
        textDalgonaLatte.focus()
    else:
        textDalgonaLatte.config(state= DISABLED)
        txtDalgonaLatte.set("0")

def blackSesamLatte():
    if var20.get()==1:
        textBlackSesamLatte.config(state= NORMAL)
        textBlackSesamLatte.delete(0, END)
        textBlackSesamLatte.focus()
    else:
        textBlackSesamLatte.config(state= DISABLED)
        txtBlackSesamLatte.set("0")

def injeolmiOatLatte():
    if var21.get()==1:
        textInjeolmiOatLatte.config(state= NORMAL)
        textInjeolmiOatLatte.delete(0, END)
        textInjeolmiOatLatte.focus()
    else:
        textInjeolmiOatLatte.config(state= DISABLED)
        txtInjeolmiOatLatte.set("0")

def pistacchioOatLatte():
    if var22.get()==1:
        textPistacchioOatLatte.config(state= NORMAL)
        textPistacchioOatLatte.delete(0, END)
        textPistacchioOatLatte.focus()
    else:
        textPistacchioOatLatte.config(state= DISABLED)
        txtPistacchioOatLatte.set("0")       


#design of the main screen
screen = Tk()
screen.title("Our Coffee system ")
screen.geometry("1300x720")
screen.resizable(0,0)
screen.config(bg="darkblue")

#setting up the fonts for the titles
Title = ("arial black", 25)
Subtitle = ("consolas", 14)

#main title frame
upperFrame = Frame(screen, bd=12, relief=RIDGE, bg="blue")
upperFrame.pack(side=TOP)
#main title
mainTitle= Label(upperFrame, text="Our Coffee System", font=Title, fg="white", bg="blue", width=53)
mainTitle.grid(row=0, column=0)

#secondary frames
menuFrame= Frame(screen, bd=10, relief=RIDGE, bg="blue")
menuFrame.pack(side=LEFT, fill=Y)
costFrame= Frame(menuFrame, bd=2, relief=RIDGE, bg="blue")
costFrame.pack(side=BOTTOM)
teaFrame= LabelFrame(menuFrame, text="Tea", bd=5, font=Subtitle, relief=RIDGE, bg="lightgray")
teaFrame.pack(side=LEFT, fill=Y)
noncoffeeFrame= LabelFrame(menuFrame, text="Non-Coffee", bd=5, font=Subtitle, relief=RIDGE, bg="lightgray")
noncoffeeFrame.pack(side=LEFT, fill=Y)
coffeeFrame= LabelFrame(menuFrame, text="Coffee", bd=5, font=Subtitle, relief=RIDGE, bg="lightgray")
coffeeFrame.pack(side=LEFT, fill=Y)

#right frames
rightFrame= Frame(screen, bd=10, relief=RIDGE, bg="blue")
rightFrame.pack(side=RIGHT)
calculatorFrame= Frame(rightFrame, bd=5, relief=RIDGE, bg="blue")
calculatorFrame.pack()
receiptFrame= Frame(rightFrame, bd=5, relief=RIDGE, bg="blue")
receiptFrame.pack()
buttonsFrame= Frame(rightFrame, bd=5, relief=RIDGE, bg="blue")
buttonsFrame.pack()

#variables
#variables for tea
var1= IntVar()
var2= IntVar()
var3= IntVar()
var4= IntVar()
var5= IntVar()
var6= IntVar()
var7= IntVar()
#variables for non-coffee
var8= IntVar()
var9= IntVar()
var10= IntVar()
#variables for coffee
var11= IntVar()
var12= IntVar()
var13= IntVar()
var14= IntVar()
var15= IntVar()
var16= IntVar()
var17= IntVar()
var18= IntVar()
var19= IntVar()
var20= IntVar()
var21= IntVar()
var22= IntVar()

#variables for text entries
#tea
txtYuzu= StringVar()
txtYuzu.set("0")
txtHintGinger= StringVar()
txtHintGinger.set("0")
txtJujubeGoji= StringVar()
txtJujubeGoji.set("0")
txtLycheeOolong= StringVar()
txtLycheeOolong.set("0")
txtGuavaJasmin= StringVar()
txtGuavaJasmin.set("0")
txtBlackLemon= StringVar()
txtBlackLemon.set("0")
txtMatchaLemon= StringVar()
txtMatchaLemon.set("0")
#non-coffe
txtChocolate= StringVar()
txtChocolate.set("0")
txtMatchaLatte= StringVar()
txtMatchaLatte.set("0")
txtUbeOatLatte= StringVar()
txtUbeOatLatte.set("0")
#coffee
txtEspresso= StringVar()
txtEspresso.set("0")
txtDoubleEspresso= StringVar()
txtDoubleEspresso.set("0")
txtAmericano= StringVar()
txtAmericano.set("0")
txtCapuccino= StringVar()
txtCapuccino.set("0")
txtFlatWhite= StringVar()
txtFlatWhite.set("0")
txtLatte= StringVar()
txtLatte.set("0")
txtMocha= StringVar()
txtMocha.set("0")
txtBiscoffLatte= StringVar()
txtBiscoffLatte.set("0")
txtDalgonaLatte= StringVar()
txtDalgonaLatte.set("0")
txtBlackSesamLatte= StringVar()
txtBlackSesamLatte.set("0")
txtInjeolmiOatLatte= StringVar()
txtInjeolmiOatLatte.set("0")
txtPistacchioOatLatte= StringVar()
txtPistacchioOatLatte.set("0")

#variables for subtotal and total
varTeaCost= StringVar()
varNoncoffeCost= StringVar()
varCoffeeCost= StringVar()
varSubtotal= StringVar()
varIVA= StringVar()
varTotal= StringVar()

#tea
#label and select button
Yuzu= Checkbutton(teaFrame, text="Yuzu", font=Subtitle, onvalue=1, offvalue=0, variable=var1, command=yuzu)
Yuzu.grid(row=0, column=0, sticky=W)
HintGinger= Checkbutton(teaFrame, text="Hint Ginger", font=Subtitle, onvalue=1, offvalue=0, variable=var2, command=hintGinger)
HintGinger.grid(row=1, column=0, sticky=W)
JujubeGoji= Checkbutton(teaFrame, text="Jujube Goji", font=Subtitle, onvalue=1, offvalue=0, variable=var3, command=jujubeGoji)
JujubeGoji.grid(row=2, column=0, sticky=W)
LycheeOolong= Checkbutton(teaFrame, text="Lychee Oolong", font=Subtitle, onvalue=1, offvalue=0, variable=var4, command=lycheeOolong)
LycheeOolong.grid(row=3, column=0, sticky=W)
GuavaJasmin= Checkbutton(teaFrame, text="Guava Jasmin", font=Subtitle, onvalue=1, offvalue=0, variable=var5, command=guavaJasmin)
GuavaJasmin.grid(row=4, column=0, sticky=W)
BlackLemon= Checkbutton(teaFrame, text="Black Lemon", font=Subtitle, onvalue=1, offvalue=0, variable=var6, command=blackLemon)
BlackLemon.grid(row=5, column=0, sticky=W)
MatchaLemon= Checkbutton(teaFrame, text="Matcha Lemon", font=Subtitle, onvalue=1, offvalue=0, variable=var7, command=matchaLemon)
MatchaLemon.grid(row=6, column=0, sticky=W)
#text boxes for each tea
textYuzu= Entry(teaFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtYuzu)
textYuzu.grid(row=0, column=1)
textHintGinger= Entry(teaFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtHintGinger)
textHintGinger.grid(row=1, column=1)
textJujubeGoji= Entry(teaFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtJujubeGoji)
textJujubeGoji.grid(row=2, column=1)
textLycheeOolong= Entry(teaFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtLycheeOolong)
textLycheeOolong.grid(row=3, column=1)
textGuavaJasmin= Entry(teaFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtGuavaJasmin)
textGuavaJasmin.grid(row=4, column=1)
textBlackLemon= Entry(teaFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtBlackLemon)
textBlackLemon.grid(row=5, column=1)
textMatchaLemon= Entry(teaFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtMatchaLemon)
textMatchaLemon.grid(row=6, column=1)

#non-coffee
#label and select button
Chocolate= Checkbutton(noncoffeeFrame, text="Chocolate", font=Subtitle, onvalue=1, offvalue=0, variable=var8, command=chocolate)
Chocolate.grid(row=0, column=0, sticky=W)
MatchaLatte= Checkbutton(noncoffeeFrame, text="Matcha Latte", font=Subtitle, onvalue=1, offvalue=0, variable=var9, command=matchaLatte)
MatchaLatte.grid(row=1, column=0, sticky=W)
UbeOatLatte= Checkbutton(noncoffeeFrame, text="Ube Oat Latte", font=Subtitle, onvalue=1, offvalue=0, variable=var10, command=ubeOatLatte)
UbeOatLatte.grid(row=2, column=0, sticky=W)
#text boxes for each non-coffee
textChocolate= Entry(noncoffeeFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtChocolate)
textChocolate.grid(row=0, column=1)
textMatchaLatte= Entry(noncoffeeFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtMatchaLatte)
textMatchaLatte.grid(row=1, column=1)
textUbeOatLatte= Entry(noncoffeeFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtUbeOatLatte)
textUbeOatLatte.grid(row=2, column=1)

#coffee
#label and select button
Espresso= Checkbutton(coffeeFrame, text="Espresso", font=Subtitle, onvalue=1, offvalue=0, variable=var11, command=espresso)
Espresso.grid(row=0, column=0, sticky=W)
DoubleEspresso= Checkbutton(coffeeFrame, text="Double Espresso", font=Subtitle, onvalue=1, offvalue=0, variable=var12, command=doubleEspresso)
DoubleEspresso.grid(row=1, column=0, sticky=W)
Americano= Checkbutton(coffeeFrame, text="Americano", font=Subtitle, onvalue=1, offvalue=0, variable=var13, command=americano)
Americano.grid(row=2, column=0, sticky=W)
Capuccino= Checkbutton(coffeeFrame, text="Capuccino", font=Subtitle, onvalue=1, offvalue=0, variable=var14, command=capuccino)
Capuccino.grid(row=3, column=0, sticky=W)
FlatWhite= Checkbutton(coffeeFrame, text="Flat White", font=Subtitle, onvalue=1, offvalue=0, variable=var15, command=flatWhite)
FlatWhite.grid(row=4, column=0, sticky=W)
Latte= Checkbutton(coffeeFrame, text="Latte", font=Subtitle, onvalue=1, offvalue=0, variable=var16, command=latte)
Latte.grid(row=5, column=0, sticky=W)
Mocha= Checkbutton(coffeeFrame, text="Mocha", font=Subtitle, onvalue=1, offvalue=0, variable=var17, command=mocha)
Mocha.grid(row=6, column=0, sticky=W)
BiscoffLatte= Checkbutton(coffeeFrame, text="Biscoff Latte", font=Subtitle, onvalue=1, offvalue=0, variable=var18, command=biscoffLatte)
BiscoffLatte.grid(row=7, column=0, sticky=W)
DalgonaLatte= Checkbutton(coffeeFrame, text="Dalgona Latte", font=Subtitle, onvalue=1, offvalue=0, variable=var19, command=dalgonaLatte)
DalgonaLatte.grid(row=8, column=0, sticky=W)
BlackSesamLatte= Checkbutton(coffeeFrame, text="Black Sesam Latte", font=Subtitle, onvalue=1, offvalue=0, variable=var20, command=blackSesamLatte)
BlackSesamLatte.grid(row=9, column=0, sticky=W)
InjeolmiOatLatte= Checkbutton(coffeeFrame, text="Injeolmi Oat Latte", font=Subtitle, onvalue=1, offvalue=0, variable=var21, command=injeolmiOatLatte)
InjeolmiOatLatte.grid(row=10, column=0, sticky=W)
PistacchioOatLatte= Checkbutton(coffeeFrame, text="Pistacchio Oat Latte", font=Subtitle, onvalue=1, offvalue=0, variable=var22, command=pistacchioOatLatte)
PistacchioOatLatte.grid(row=11, column=0, sticky=W)
#text boxes for each coffee
textEspresso= Entry(coffeeFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtEspresso)
textEspresso.grid(row=0, column=1)
textDoubleEspresso= Entry(coffeeFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtDoubleEspresso)
textDoubleEspresso.grid(row=1, column=1)
textAmericano= Entry(coffeeFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtAmericano)
textAmericano.grid(row=2, column=1)
textCapuccino= Entry(coffeeFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtCapuccino)
textCapuccino.grid(row=3, column=1)
textFlatWhite= Entry(coffeeFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtFlatWhite)
textFlatWhite.grid(row=4, column=1)
textLatte= Entry(coffeeFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtLatte)
textLatte.grid(row=5, column=1)
textMocha= Entry(coffeeFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtMocha)
textMocha.grid(row=6, column=1)
textBiscoffLatte= Entry(coffeeFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtBiscoffLatte)
textBiscoffLatte.grid(row=7, column=1)
textDalgonaLatte= Entry(coffeeFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtDalgonaLatte)
textDalgonaLatte.grid(row=8, column=1)
textBlackSesamLatte= Entry(coffeeFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtBlackSesamLatte)
textBlackSesamLatte.grid(row=9, column=1)
textInjeolmiOatLatte= Entry(coffeeFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtInjeolmiOatLatte)
textInjeolmiOatLatte.grid(row=10, column=1)
textPistacchioOatLatte= Entry(coffeeFrame, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtPistacchioOatLatte)
textPistacchioOatLatte.grid(row=11, column=1)

#total labels and input entries for values
teaCost= Label(costFrame, text="Total in tea", font=Subtitle, bd=10, bg="blue", fg="white")
teaCost.grid(row=0, column=0)
checkboxTeaCost= Entry(costFrame, font=Subtitle, bd=10, width=14, state="readonly")
checkboxTeaCost.grid(row=0, column=1, padx=5)
noncoffeeCost= Label(costFrame, text="Total in Non-Coffee", font=Subtitle, bd=10, width=14, bg="blue", fg="white")
noncoffeeCost.grid(row=1, column=0)
checkboxNoncoffeeCost= Entry(costFrame, font=Subtitle, bd=10, width=14, fg="white", bg="blue", state="readonly")
checkboxNoncoffeeCost.grid(row=1, column=1)
coffeeCost= Label(costFrame, font=Subtitle, text="Total in Coffee", bd=10, bg="blue", fg="white")
coffeeCost.grid(row=2, column=0)
checkboxCoffeeCost= Entry(costFrame, font=Subtitle, state="readonly", bd=10, width=14)
checkboxCoffeeCost.grid(row=2, column=1)

subtotal= Label(costFrame, text="Subtotal", font=Subtitle, bd=10, bg="blue", fg="white")
subtotal.grid(row=0, column=2)
checkboxSubtotal= Entry(costFrame, font=Subtitle, bd=10, width=14, state="readonly")
checkboxSubtotal.grid(row=0, column=3, padx=41)
iva= Label(costFrame, text="IVA", font=Subtitle, bd=10, width=14, bg="blue", fg="white")
iva.grid(row=1, column=2)
checkboxIVA= Entry(costFrame, font=Subtitle, bd=10, width=14, fg="white", bg="blue", state="readonly")
checkboxIVA.grid(row=1, column=3)
total= Label(costFrame, font=Subtitle, text="Total", bd=10, bg="blue", fg="white")
total.grid(row=2, column=2)
checkboxTotal= Entry(costFrame, font=Subtitle, state="readonly", bd=10, width=14)
checkboxTotal.grid(row=2, column=3)

#calculator programming
operation=""

def clickbutton(numbers):
    global operation
    operation= operation+numbers
    screenCalculator.delete(0, END)
    screenCalculator.insert(END, operation)

def clear():
    global operation
    operation=""
    screenCalculator.delete(0, END)

def result():
    global operation
    result= str(eval(operation))
    screenCalculator.delete(0, END)
    screenCalculator.insert(0, result)
    operation=""

#calculator
screenCalculator= Entry(calculatorFrame, font=("arial", 18, "bold"), width=44, bd=4)
screenCalculator.grid(row=0, column=0, columnspan=4, pady=10)
#calculator buttons
button7= Button(calculatorFrame, text="7", font=Subtitle, fg="black", bg="blue", bd=6, width=9, command=lambda:clickbutton("7")).grid(row=1, column=0)
button8= Button(calculatorFrame, text="8", font=Subtitle, fg="black", bg="blue", bd=6, width=9, command=lambda:clickbutton("8")).grid(row=1, column=1)
button9= Button(calculatorFrame, text="9", font=Subtitle, fg="black", bg="blue", bd=6, width=9, command=lambda:clickbutton("9")).grid(row=1, column=2)
buttonPlus= Button(calculatorFrame, text="+", font=Subtitle, fg="blue", bg="lightgray", bd=6, width=9, command=lambda:clickbutton("+")).grid(row=1, column=3)

button4= Button(calculatorFrame, text="4", font=Subtitle, fg="black", bg="blue", bd=6, width=9, command=lambda:clickbutton("4")).grid(row=2, column=0)
button5= Button(calculatorFrame, text="5", font=Subtitle, fg="black", bg="blue", bd=6, width=9, command=lambda:clickbutton("5")).grid(row=2, column=1)
button6= Button(calculatorFrame, text="6", font=Subtitle, fg="black", bg="blue", bd=6, width=9, command=lambda:clickbutton("6")).grid(row=2, column=2)
buttonMinus= Button(calculatorFrame, text="-", font=Subtitle, fg="blue", bg="lightgray", bd=6, width=9, command=lambda:clickbutton("-")).grid(row=2, column=3)

button1= Button(calculatorFrame, text="1", font=Subtitle, fg="black", bg="blue", bd=6, width=9, command=lambda:clickbutton("1")).grid(row=3, column=0)
button2= Button(calculatorFrame, text="2", font=Subtitle, fg="black", bg="blue", bd=6, width=9, command=lambda:clickbutton("2")).grid(row=3, column=1)
button3= Button(calculatorFrame, text="3", font=Subtitle, fg="black", bg="blue", bd=6, width=9, command=lambda:clickbutton("3")).grid(row=3, column=2)
buttonMultiply= Button(calculatorFrame, text="*", font=Subtitle, fg="blue", bg="lightgray", bd=6, width=9, command=lambda:clickbutton("*")).grid(row=3, column=3)

buttonEqual= Button(calculatorFrame, text="=", font=Subtitle, fg="blue", bg="lightgray", bd=6, width=9, command=result).grid(row=4, column=0)
buttonClear= Button(calculatorFrame, text="C", font=Subtitle, fg="blue", bg="lightgray", bd=6, width=9, command=clear).grid(row=4, column=1)
button0= Button(calculatorFrame, text="0", font=Subtitle, fg="blue", bg="lightgray", bd=6, width=9, command=lambda:clickbutton("0")).grid(row=4, column=2)
buttonDivide= Button(calculatorFrame, text="/", font=Subtitle, fg="blue", bg="lightgray", bd=6, width=9, command=lambda:clickbutton("/")).grid(row=4, column=3)

#receipt
receiptText= Text(receiptFrame, font=("arial", 12, "bold"), bd=3, width=68, height=12)
receiptText.grid(row=0, column=0)
#buttons
totalButton= Button(buttonsFrame, text="Total", font=Subtitle, fg="black", bg="blue", bd=4, padx=12, command=grantotal).grid(row=0, column=0)
receiptButton= Button(buttonsFrame, text="Receipt", font=Subtitle, fg="black", bg="blue", bd=4, padx=12, command=receipt).grid(row=0, column=1)
saveButton= Button(buttonsFrame, text="Save", font=Subtitle, fg="black", bg="blue", bd=4, padx=12, command=save).grid(row=0, column=2)
clearButton= Button(buttonsFrame, text="Clear", font=Subtitle, fg="black", bg="blue", bd=4, padx=12, command=delete).grid(row=0, column=4)


screen.mainloop()
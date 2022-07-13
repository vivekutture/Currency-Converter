#Step 1 : Install tkinter : pip install tkinter / pip install tk
#Step 2 : Install request : pip install requests
# MANDATORY : "INTERNET" connectivity is required because this real time Currency Convrter


from tkinter import *
from tkinter import ttk
from tkinter import messagebox  
import requests
currency_converter =Tk()
currency_converter.title("Currency Converter")
currency_converter.geometry('502x350')
base_url = 'https://open.er-api.com/v6/latest/USD'
response = requests.get(base_url).json()
cur=response['rates']  
currency=sorted(list(cur.keys()))
cb1=ttk.Combobox(currency_converter,values=currency,state="readonly",width=17,font=("Arial Rounded MT Bold",16),justify=CENTER)
cb2=ttk.Combobox(currency_converter,values=currency,state="readonly",width=17,font=("Arial Rounded MT Bold",16),justify=CENTER)
cb1.grid(column=0, row=1,pady=20)
cb2.grid(column=1, row=1,pady=20)
cb1.set("Select")
cb2.set("Select")
cb1.config(width=19)
cb2.config(width=19)
def curcal():
    try:        
        amt=float(textbox1.get())
        from_cur = str(cb1.get())
        to_cur = str(cb2.get())
        if from_cur != 'USD' : 
            amt = amt / cur[from_cur] 
        amt = round(amt * cur[to_cur], 4)
        l2.config(text=str(amt))
    except:
        currency_converter.withdraw()
        messagebox.showerror("ERROR","Invalid Operation")
        currency_converter.destroy()
        exit()

def clear():
    textbox1.delete(0, END)
    l2.config(text='')
    cb1.set("Select")
    cb2.set("Select")
        
textbox1 = Entry(currency_converter,font=("Arial Rounded MT Bold",14),justify = CENTER,bd = 3, relief = RIDGE,width=17)
textbox1.grid(column=0, row=2)    
l2 = Label(currency_converter,text ='', fg = 'black', bg = 'white', relief = RIDGE, justify = CENTER,bd=3,width=17,font=("Arial Rounded MT Bold",14))
l2.grid(column=1, row=2)
b1=Button(currency_converter,text="CONVERT",command=curcal,fg='black',font=("Copperplate Gothic Bold",14))
b1.grid(column=1, row=7,pady=20)
b2=Button(currency_converter,text="CLEAR",command=clear,fg='black',font=("Copperplate Gothic Bold",14))
b2.grid(column=0, row=7,pady=20)
currency_converter.mainloop()

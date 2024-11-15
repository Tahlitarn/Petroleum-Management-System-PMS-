import os
import sys
from tkinter import *
from tkinter import PhotoImage
from tkinter import filedialog
from datetime import date
from tkinter import messagebox, Message
from fpdf import FPDF

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

home=Tk()
home.title(' ')
home.iconbitmap(resource_path('C:/Users/user/Desktop/PMS/img/img_logo.ico'))
app_width = 1220
app_height = 630
screen_width = home.winfo_screenwidth()
screen_height = home.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
home.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
home.resizable(width=False, height=False)
home.anchor(CENTER)
# home.overrideredirect(1)


# declaration of some variables
global gen_price 
global l2,l3,l4,l5,b2,b3,b4,b5,z1,z2,z3,z4,d1,d2,d3,d4,e1,e2,e3,e4,f1,f2,f3,f4
global x1,x2,x3,x4,y1,y2,y3,y4

img=PhotoImage(file=(resource_path("C:/Users/user/Desktop//PMS/img/front_view2.png")))
#______________________________________________________________FRAMES FOR THE PROJECTS_________________________________________________________________________________________________
display = Label(home, text='PETROLEUM MANAGEMENT SYSTEM',width=102,
                 font=('cambria', 16,"bold"),fg="green",bg="gray")
display.pack()

main_frm=LabelFrame(home,text="BISYL OIL AND GAS",font=('cambria', 11,"bold"),fg="green",bg="gray",labelanchor="nw")
main_frm.pack()
ctrl1_screen=LabelFrame(main_frm,text="CONTROL1",borderwidth=2,background="gray",
                        font=('cambria', 12,"bold"),highlightthickness=2,highlightcolor='black',fg="black",highlightbackground="black",width=10,height=20)
ctrl1_screen.grid(row=0,column=0,padx=7)

frm_screen=LabelFrame(main_frm,text="MAIN SCREEN",borderwidth=2,background="gray",fg="black",
                      font=('cambria', 12,"bold"),highlightthickness=2,highlightcolor='black',highlightbackground="black",width=995,height=485)
frm_screen.grid(row=0,column=1)
img=PhotoImage(file=(resource_path("C:/Users/user/Desktop/PMS/img/front_view2.png")))
lbl=Label(frm_screen,image=img)
lbl.place(relheight=1,relwidth=1)

#____________________________________________________pms__screen___________________________________________________________________________________________

pms_screen=LabelFrame(frm_screen,text="P.M.S",borderwidth=2,background="gray",fg="black",
                      font=('cambria', 12,"bold"),highlightthickness=2,highlightcolor='gray',highlightbackground="black",width=1000,height=500)
pms_screen.pack_forget()

#____________________________________________________deisel__screen___________________________________________________________________________________________

deisel_screen=LabelFrame(frm_screen,text="DIESEL",borderwidth=2,background="gray",fg="black",
                      font=('cambria', 12,"bold"),highlightthickness=2,highlightcolor='black',highlightbackground="black",width=1000,height=500)
deisel_screen.pack_forget()

#____________________________________________________dpk__screen___________________________________________________________________________________________

dpk_screen=LabelFrame(frm_screen,text="KEROSINE",borderwidth=2,background="gray",fg="black",
                      font=('cambria', 12,"bold"),highlightthickness=2,highlightcolor='black',highlightbackground="black",width=1000,height=500)
dpk_screen.pack_forget()
#____________________________________________________gas__screen___________________________________________________________________________________________
gas_screen=LabelFrame(frm_screen,text="GAS",borderwidth=2,background="gray",fg="black",
                      font=('cambria', 12,"bold"),highlightthickness=2,highlightcolor='black',highlightbackground="black",width=1000,height=500)
gas_screen.pack_forget()

#____________________________________________________controls___________________________________________________________________________________________

ctrl2_screen=LabelFrame(main_frm,text="CONTROL2",borderwidth=2,background="gray",
                        font=('cambria', 12,"bold"),highlightthickness=2,highlightcolor='black',highlightbackground="black",width=10,height=20)
ctrl2_screen.grid(row=0,column=2,padx=7)

ctrl3_screen=LabelFrame(main_frm,text="CALCULATE",borderwidth=2,background="gray",
                        font=('cambria', 12,"bold"),highlightthickness=2,highlightcolor='black',highlightbackground="black",width=50,height=80)
ctrl3_screen.grid(row=1,column=1,pady=5)

#____________________________________________________________PLACING OBJECTS INSIDE THREEN______________________________________________________________


#____pump2______
pump2_frm=LabelFrame(pms_screen,text="PUMP2",border=2,borderwidth=2,background="gray",font=("caligraphy",10,"bold"),fg="black")
pump2_frm.grid(row=0,column=0,padx=5,pady=2)

pump2_lbl=Label(pump2_frm,text='Opening',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump2_lbl.grid(row=0,column=0)
pms2_open=Entry(pump2_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms2_open.focus_set()
pms2_open.grid(row=0,column=1)

pump2_lbl=Label(pump2_frm,text='Closing',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump2_lbl.grid(row=1,column=0,pady=1)
pms2_close=Entry(pump2_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms2_close.grid(row=1,column=1,pady=1)

pump2_lbl=Label(pump2_frm,text='Liter Sold',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump2_lbl.grid(row=2,column=0)
pms2_liter=Label(pump2_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pms2_liter.grid(row=2,column=1)

pump2_lbl=Label(pump2_frm,text='Amount #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump2_lbl.grid(row=3,column=0)
pms2_amount=Label(pump2_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pms2_amount.grid(row=3,column=1)

pump2_lbl=Label(pump2_frm,text='Cash #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump2_lbl.grid(row=4,column=0)
pms2_cash=Entry(pump2_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms2_cash.grid(row=4,column=1,pady=1)

pump2_lbl=Label(pump2_frm,text='Transfer #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump2_lbl.grid(row=5,column=0)
pms2_transfer=Entry(pump2_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms2_transfer.grid(row=5,column=1,pady=1)

pump2_lbl=Label(pump2_frm,text='P.O.S',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump2_lbl.grid(row=6,column=0)
pms2_pos=Entry(pump2_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms2_pos.grid(row=6,column=1,pady=1)

pump2_lbl=Label(pump2_frm,text='Expenses',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump2_lbl.grid(row=7,column=0)
pms2_expenses=Entry(pump2_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms2_expenses.grid(row=7,column=1,pady=1)

pump2_lbl=Label(pump2_frm,text='Excess',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump2_lbl.grid(row=8,column=0)
pms2_excess=Label(pump2_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pms2_excess.grid(row=8,column=1)

pump2_lbl=Label(pump2_frm,text='Shortage',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump2_lbl.grid(row=9,column=0)
pms2_short=Label(pump2_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pms2_short.grid(row=9,column=1)

#_________PMS__BUTTONs________

def pms1_c():
    x1=pms2_open.get()
    y1=pms2_close.get()
    z1=pms2_cash.get()
    d1=pms2_transfer.get()
    e1=pms2_pos.get()
    f1=pms2_expenses.get()
    p_pms = (gen_price.get())

    if x1=="" or y1=="" or  z1==""  or  d1==""  or  e1==""  or  f1==""  or p_pms=="":
        messagebox.showerror("","Input value")
    else:
        l2=round(float(y1)-float(x1),2)
        pms2_liter.config(text=f"{l2} L")
        a2=int(p_pms)
        b2=l2*a2
        pms2_amount.config(text=f"{round(b2)}")

        g1=int(z1)+int(d1)+int(e1)+int(f1)
        h1=g1-b2
        if g1 > b2:
            pms2_excess.config(text=round(h1))
            pms2_short.config(text="0.00")
            
        elif g1 < b2:
            pms2_short.config(text=round(h1))
            pms2_excess.config(text="0.00")

pms_calc=Button(pump2_frm,text="CALCULATE",font=("cambria",12,"bold"),fg="black",background="gray",borderwidth=0,justify='center',command=pms1_c)
pms_calc.grid(row=10,column=0,padx=2,pady=2)

def pms1_cls():
    pms2_open.delete(0,END)
    pms2_close.delete(0,END)
    pms2_cash.delete(0,END)
    pms2_expenses.delete(0,END)
    pms2_pos.delete(0,END)
    pms2_transfer.delete(0,END)

pms_cls=Button(pump2_frm,text="CLEAR",font=("cambria",12,"bold"),fg="black",background="gray",borderwidth=0,justify='center',command=pms1_cls)
pms_cls.grid(row=10,column=1,padx=2,pady=2)

#____pump3______
pump3_frm=LabelFrame(pms_screen,text="PUMP3",border=2,borderwidth=2,background="gray",font=("caligraphy",10,"bold"),fg="black")
pump3_frm.grid(row=0,column=1,padx=5,pady=2)

pump3_lbl=Label(pump3_frm,text='Opening',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump3_lbl.grid(row=0,column=0)
pms3_open=Entry(pump3_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
# pms_open.focus_set()
pms3_open.grid(row=0,column=1)

pump3_lbl=Label(pump3_frm,text='Closing',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump3_lbl.grid(row=1,column=0,pady=1)
pms3_close=Entry(pump3_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms3_close.grid(row=1,column=1,pady=1)

pump3_lbl=Label(pump3_frm,text='Liter Sold',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump3_lbl.grid(row=2,column=0)
pms3_liter=Label(pump3_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pms3_liter.grid(row=2,column=1)

pump3_lbl=Label(pump3_frm,text='Amount #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump3_lbl.grid(row=3,column=0)
pms3_amount=Label(pump3_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pms3_amount.grid(row=3,column=1)

pump3_lbl=Label(pump3_frm,text='Cash #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump3_lbl.grid(row=4,column=0)
pms3_cash=Entry(pump3_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms3_cash.grid(row=4,column=1,pady=1)

pump3_lbl=Label(pump3_frm,text='Transfer #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump3_lbl.grid(row=5,column=0)
pms3_transfer=Entry(pump3_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms3_transfer.grid(row=5,column=1,pady=1)

pump3_lbl=Label(pump3_frm,text='P.O.S',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump3_lbl.grid(row=6,column=0)
pms3_pos=Entry(pump3_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms3_pos.grid(row=6,column=1,pady=1)

pump3_lbl=Label(pump3_frm,text='Expenses',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump3_lbl.grid(row=7,column=0)
pms3_expenses=Entry(pump3_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms3_expenses.grid(row=7,column=1,pady=1)

pump3_lbl=Label(pump3_frm,text='Excess',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump3_lbl.grid(row=8,column=0)
pms3_excess=Label(pump3_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pms3_excess.grid(row=8,column=1)

pump3_lbl=Label(pump3_frm,text='Shortage',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump3_lbl.grid(row=9,column=0)
pms3_short=Label(pump3_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pms3_short.grid(row=9,column=1)

#_________PMS__BUTTONs________
def pms3_c():
    x2=pms3_open.get()
    y2=pms3_close.get()
    z2=pms3_cash.get()
    d2=pms3_transfer.get()
    e2=pms3_pos.get()
    f2=pms3_expenses.get()
    p_pms = (gen_price.get())

    if x2=="" or y2=="" or  z2==""  or  d2==""  or  e2==""  or  f2==""  or p_pms=="":
        messagebox.showerror("","Input value")
    else:
        l3=round(float(y2)-float(x2),2)
        pms3_liter.config(text=f"{l3} L")
        a3=int(p_pms)
        b3=l3*a3
        pms3_amount.config(text=f"{round(b3)}")

        g2=int(z2)+int(d2)+int(e2)+int(f2)
        h2=g2-b3
        if g2 > b3:
            pms3_excess.config(text=round(h2))
            pms3_short.config(text="0.00")
            
        elif g2 < b3:
            pms3_short.config(text=round(h2))
            pms3_excess.config(text="0.00")

pms_calc=Button(pump3_frm,text="CALCULATE",font=("cambria",12,"bold"),fg="black",background="gray",borderwidth=0,justify='center',command=pms3_c)
pms_calc.grid(row=10,column=0,padx=2,pady=2)

def pms3_cls():
    pms3_open.delete(0,END)
    pms3_close.delete(0,END)
    pms3_cash.delete(0,END)
    pms3_expenses.delete(0,END)
    pms3_pos.delete(0,END)
    pms3_transfer.delete(0,END)

pms_cls=Button(pump3_frm,text="CLEAR",font=("cambria",12,"bold"),fg="black",background="gray",borderwidth=0,justify='center',command=pms3_cls)
pms_cls.grid(row=10,column=1,padx=2,pady=2)

#____pump4______
pump4_frm=LabelFrame(pms_screen,text="PUMP4",border=2,borderwidth=2,background="gray",font=("caligraphy",10,"bold"),fg="black")
pump4_frm.grid(row=0,column=2,padx=5,pady=2)

pump4_lbl=Label(pump4_frm,text='Opening',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump4_lbl.grid(row=0,column=0)
pms4_open=Entry(pump4_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
# pms_open.focus_set()
pms4_open.grid(row=0,column=1)

pump4_lbl=Label(pump4_frm,text='Closing',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump4_lbl.grid(row=1,column=0,pady=1)
pms4_close=Entry(pump4_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms4_close.grid(row=1,column=1,pady=1)

pump4_lbl=Label(pump4_frm,text='Liter Sold',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump4_lbl.grid(row=2,column=0)
pms4_liter=Label(pump4_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pms4_liter.grid(row=2,column=1)

pump4_lbl=Label(pump4_frm,text='Amount #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump4_lbl.grid(row=3,column=0)
pms4_amount=Label(pump4_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pms4_amount.grid(row=3,column=1)

pump4_lbl=Label(pump4_frm,text='Cash #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump4_lbl.grid(row=4,column=0)
pms4_cash=Entry(pump4_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms4_cash.grid(row=4,column=1,pady=1)

pump4_lbl=Label(pump4_frm,text='Transfer #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump4_lbl.grid(row=5,column=0)
pms4_transfer=Entry(pump4_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms4_transfer.grid(row=5,column=1,pady=1)

pump4_lbl=Label(pump4_frm,text='P.O.S',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump4_lbl.grid(row=6,column=0)
pms4_pos=Entry(pump4_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms4_pos.grid(row=6,column=1,pady=1)

pump4_lbl=Label(pump4_frm,text='Expenses',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump4_lbl.grid(row=7,column=0)
pms4_expenses=Entry(pump4_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms4_expenses.grid(row=7,column=1,pady=1)

pump4_lbl=Label(pump4_frm,text='Excess',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump4_lbl.grid(row=8,column=0)
pms4_excess=Label(pump4_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pms4_excess.grid(row=8,column=1)

pump4_lbl=Label(pump4_frm,text='Shortage',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump4_lbl.grid(row=9,column=0)
pms4_short=Label(pump4_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pms4_short.grid(row=9,column=1)

#_________PMS__BUTTONs________
def pms4_c():
    x3=pms4_open.get()
    y3=pms4_close.get()
    z3=pms4_cash.get()
    d3=pms4_transfer.get()
    e3=pms4_pos.get()
    f3=pms4_expenses.get()
    p_pms = (gen_price.get())

    if x3=="" or y3=="" or  z3==""  or  d3==""  or  e3==""  or  f3==""  or p_pms=="":
        messagebox.showerror("","Input value")
    else:
        l4=round(float(y3)-float(x3),2)
        pms4_liter.config(text=f"{l4} L")
        a4=int(p_pms)
        b4=l4*a4
        pms4_amount.config(text=f"{round(b4)}")

        g3=int(z3)+int(d3)+int(e3)+int(f3)
        h3=g3-b4
        if g3 > b4:
            pms4_excess.config(text=round(h3))
            pms4_short.config(text="0.00")
            
        elif g3 < b4:
            pms4_short.config(text=round(h3))
            pms4_excess.config(text="0.00")

pms_calc=Button(pump4_frm,text="CALCULATE",font=("cambria",12,"bold"),fg="black",background="gray",borderwidth=0,justify='center',command=pms4_c)
pms_calc.grid(row=10,column=0,padx=2,pady=2)

def pms4_cls():
    pms4_open.delete(0,END)
    pms4_close.delete(0,END)
    pms4_cash.delete(0,END)
    pms4_expenses.delete(0,END)
    pms4_pos.delete(0,END)
    pms4_transfer.delete(0,END)

pms_cls=Button(pump4_frm,text="CLEAR",font=("cambria",12,"bold"),fg="black",background="gray",borderwidth=0,justify='center',command=pms4_cls)
pms_cls.grid(row=10,column=1,padx=2,pady=2)

#____pump5______
pump5_frm=LabelFrame(pms_screen,text="PUMP5",border=2,borderwidth=2,background="gray",font=("caligraphy",10,"bold"),fg="black")
pump5_frm.grid(row=0,column=3,padx=5,pady=2)

pump5_lbl=Label(pump5_frm,text='Opening',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump5_lbl.grid(row=0,column=0)
pms5_open=Entry(pump5_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
# pms_open.focus_set()
pms5_open.grid(row=0,column=1)

pump5_lbl=Label(pump5_frm,text='Closing',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump5_lbl.grid(row=1,column=0,pady=1)
pms5_close=Entry(pump5_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms5_close.grid(row=1,column=1,pady=1)

pump5_lbl=Label(pump5_frm,text='Liter Sold',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump5_lbl.grid(row=2,column=0)
pms5_liter=Label(pump5_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pms5_liter.grid(row=2,column=1)

pump5_lbl=Label(pump5_frm,text='Amount #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump5_lbl.grid(row=3,column=0)
pms5_amount=Label(pump5_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pms5_amount.grid(row=3,column=1)

pump5_lbl=Label(pump5_frm,text='Cash #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump5_lbl.grid(row=4,column=0)
pms5_cash=Entry(pump5_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms5_cash.grid(row=4,column=1,pady=1)

pump5_lbl=Label(pump5_frm,text='Transfer #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump5_lbl.grid(row=5,column=0)
pms5_transfer=Entry(pump5_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms5_transfer.grid(row=5,column=1,pady=1)

pump5_lbl=Label(pump5_frm,text='P.O.S',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump5_lbl.grid(row=6,column=0)
pms5_pos=Entry(pump5_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms5_pos.grid(row=6,column=1,pady=1)

pump5_lbl=Label(pump5_frm,text='Expenses',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump5_lbl.grid(row=7,column=0)
pms5_expenses=Entry(pump5_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
pms5_expenses.grid(row=7,column=1,pady=1)

pump5_lbl=Label(pump5_frm,text='Excess',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump5_lbl.grid(row=8,column=0)
pms5_excess=Label(pump5_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pms5_excess.grid(row=8,column=1)

pump5_lbl=Label(pump5_frm,text='Shortage',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump5_lbl.grid(row=9,column=0)
pms5_short=Label(pump5_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pms5_short.grid(row=9,column=1)

#_________PMS__BUTTONs________
def pms5_c():
    x4=pms5_open.get()
    y4=pms5_close.get()
    z4=pms5_cash.get()
    d4=pms5_transfer.get()
    e4=pms5_pos.get()
    f4=pms5_expenses.get()
    p_pms = (gen_price.get())

    if x4=="" or y4=="" or  z4==""  or  d4==""  or  e4==""  or  f4==""  or p_pms=="":
        messagebox.showerror("","Input value")
    else:
        l5=round(float(y4)-float(x4),2)
        pms5_liter.config(text=f"{l5} L")
        a5=int(p_pms)
        b5=l5*a5
        pms5_amount.config(text=f"{round(b5)}")

        g4=int(z4)+int(d4)+int(e4)+int(f4)
        h4=g4-b5
        if g4 > b5:
            pms5_excess.config(text=round(h4))
            pms5_short.config(text="0.00")
            
        elif g4 < b5:
            pms5_short.config(text=round(h4))
            pms5_excess.config(text="0.00")

pms_calc=Button(pump5_frm,text="CALCULATE",font=("cambria",12,"bold"),fg="black",background="gray",borderwidth=0,justify='center',command=pms5_c)
pms_calc.grid(row=10,column=0,padx=2,pady=2)

def pms5_cls():
    pms5_open.delete(0,END)
    pms5_close.delete(0,END)
    pms5_cash.delete(0,END)
    pms5_expenses.delete(0,END)
    pms5_pos.delete(0,END)
    pms5_transfer.delete(0,END)

pms_cls=Button(pump5_frm,text="CLEAR",font=("cambria",12,"bold"),fg="black",background="gray",borderwidth=0,justify='center',command=pms5_cls)
pms_cls.grid(row=10,column=1,padx=2,pady=2)

# ___________________________________deisel______________________________________________________________________________________________________________
pump_deisel_frm=LabelFrame(deisel_screen,text="A.G.O",border=2,borderwidth=2,background="gray",font=("caligraphy",10,"bold"),fg="black")
pump_deisel_frm.grid(row=0,column=3,padx=5,pady=2)

pump_deisel_lbl=Label(pump_deisel_frm,text='Opening',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_deisel_lbl.grid(row=0,column=0)
deisel_open=Entry(pump_deisel_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
# pms_open.focus_set()
deisel_open.grid(row=0,column=1)

pump_deisel_lbl=Label(pump_deisel_frm,text='Closing',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_deisel_lbl.grid(row=1,column=0,pady=1)
deisel_close=Entry(pump_deisel_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
deisel_close.grid(row=1,column=1,pady=1)

pump_deisel_lbl=Label(pump_deisel_frm,text='Liter Sold',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_deisel_lbl.grid(row=2,column=0)
deisel_liter=Label(pump_deisel_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
deisel_liter.grid(row=2,column=1)

pump_deisel_lbl=Label(pump_deisel_frm,text='Amount #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_deisel_lbl.grid(row=3,column=0)
deisel_amount=Label(pump_deisel_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
deisel_amount.grid(row=3,column=1)

pump_deisel_lbl=Label(pump_deisel_frm,text='Cash #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_deisel_lbl.grid(row=4,column=0)
deisel_cash=Entry(pump_deisel_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
deisel_cash.grid(row=4,column=1,pady=1)

pump_deisel_lbl=Label(pump_deisel_frm,text='Transfer #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_deisel_lbl.grid(row=5,column=0)
deisel_transfer=Entry(pump_deisel_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
deisel_transfer.grid(row=5,column=1,pady=1)

pump_deisel_lbl=Label(pump_deisel_frm,text='P.O.S',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_deisel_lbl.grid(row=6,column=0)
deisel_pos=Entry(pump_deisel_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
deisel_pos.grid(row=6,column=1,pady=1)

pump_deisel_lbl=Label(pump_deisel_frm,text='Expenses',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_deisel_lbl.grid(row=7,column=0)
deisel_expenses=Entry(pump_deisel_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
deisel_expenses.grid(row=7,column=1,pady=1)

pump_deisel_lbl=Label(pump_deisel_frm,text='Excess',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_deisel_lbl.grid(row=8,column=0)
deisel_excess=Label(pump_deisel_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
deisel_excess.grid(row=8,column=1)

pump_deisel_lbl=Label(pump_deisel_frm,text='Shortage',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_deisel_lbl.grid(row=9,column=0)
deisel_short=Label(pump_deisel_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
deisel_short.grid(row=9,column=1)

deisel_price_lbl=Label(pump_deisel_frm,text='PRICE',font=("cambria",12,"bold","italic"),fg="black",background="gray")
deisel_price_lbl.grid(row=10,column=0)
deisel_price_txt=Entry(pump_deisel_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
deisel_price_txt.grid(row=10,column=1,pady=1)

#_________DEISEL__BUTTONs________
def deisel_c():
    x5=deisel_open.get()
    y5=deisel_close.get()
    z5=deisel_cash.get()
    d5=deisel_transfer.get()
    e5=deisel_pos.get()
    f5=deisel_expenses.get()
    d_pms = (deisel_price_txt.get())

    if x5=="" or y5=="" or  z5==""  or  d5==""  or  e5==""  or  f5==""  or d_pms=="":
        messagebox.showerror("","Input value")
    else:
        l6=round(float(y5)-float(x5),2)
        deisel_liter.config(text=f"{l6} L")
        a6=int(d_pms)
        b6=l6*a6
        deisel_amount.config(text=f"{round(b6)}")

        g5=int(z5)+int(d5)+int(e5)+int(f5)
        h5=g5-b6
        if g5 > b6:
            deisel_excess.config(text=round(h5))
            deisel_short.config(text="0.00")
            
        elif g5 < b6:
            deisel_short.config(text=round(h5))
            deisel_excess.config(text="0.00")

diesel_calc=Button(pump_deisel_frm,text="CALCULATE",font=("cambria",12,"bold"),fg="black",background="gray",borderwidth=0,justify='center',command=deisel_c)
diesel_calc.grid(row=11,column=0,padx=2,pady=2)

def deisel_cls():
    deisel_open.delete(0,END)
    deisel_close.delete(0,END)
    deisel_cash.delete(0,END)
    deisel_expenses.delete(0,END)
    deisel_pos.delete(0,END)
    deisel_transfer.delete(0,END)

diesel_clc=Button(pump_deisel_frm,text="CLEAR",font=("cambria",12,"bold"),fg="black",background="gray",borderwidth=0,justify='center',command=deisel_cls)
diesel_clc.grid(row=11,column=1,padx=2,pady=2)

# ___________________________________dpk______________________________________________________________________________________________________________
pump_dpk_frm=LabelFrame(dpk_screen,text="DPK",border=2,borderwidth=2,background="gray",font=("caligraphy",10,"bold"),fg="black")
pump_dpk_frm.grid(row=0,column=3,padx=5,pady=2)

pump_dpk_lbl=Label(pump_dpk_frm,text='Opening',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_dpk_lbl.grid(row=0,column=0)
dpk_open=Entry(pump_dpk_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
# pms_open.focus_set()
dpk_open.grid(row=0,column=1)

pump_dpk_lbl=Label(pump_dpk_frm,text='Closing',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_dpk_lbl.grid(row=1,column=0,pady=1)
dpk_close=Entry(pump_dpk_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
dpk_close.grid(row=1,column=1,pady=1)

pump_dpk_lbl=Label(pump_dpk_frm,text='Liter Sold',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_dpk_lbl.grid(row=2,column=0)
dpk_liter=Label(pump_dpk_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
dpk_liter.grid(row=2,column=1)

pump_dpk_lbl=Label(pump_dpk_frm,text='Amount #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_dpk_lbl.grid(row=3,column=0)
dpk_amount=Label(pump_dpk_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
dpk_amount.grid(row=3,column=1)

pump_dpk_lbl=Label(pump_dpk_frm,text='Cash #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_dpk_lbl.grid(row=4,column=0)
dpk_cash=Entry(pump_dpk_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
dpk_cash.grid(row=4,column=1,pady=1)

pump_dpk_lbl=Label(pump_dpk_frm,text='Transfer #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_dpk_lbl.grid(row=5,column=0)
dpk_transfer=Entry(pump_dpk_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
dpk_transfer.grid(row=5,column=1,pady=1)

pump_dpk_lbl=Label(pump_dpk_frm,text='P.O.S',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_dpk_lbl.grid(row=6,column=0)
dpk_pos=Entry(pump_dpk_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
dpk_pos.grid(row=6,column=1,pady=1)

pump_dpk_lbl=Label(pump_dpk_frm,text='Expenses',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_dpk_lbl.grid(row=7,column=0)
dpk_expenses=Entry(pump_dpk_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
dpk_expenses.grid(row=7,column=1,pady=1)

pump_dpk_lbl=Label(pump_dpk_frm,text='Excess',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_dpk_lbl.grid(row=8,column=0)
dpk_excess=Label(pump_dpk_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
dpk_excess.grid(row=8,column=1)

pump_dpk_lbl=Label(pump_dpk_frm,text='Shortage',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_dpk_lbl.grid(row=9,column=0)
dpk_short=Label(pump_dpk_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
dpk_short.grid(row=9,column=1)

dpk_price_lbl=Label(pump_dpk_frm,text='PRICE',font=("cambria",12,"bold","italic"),fg="black",background="gray")
dpk_price_lbl.grid(row=10,column=0)
dpk_price_txt=Entry(pump_dpk_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
dpk_expenses.grid(row=10,column=1,pady=1)

#_________DPK__BUTTONs________
def dpk_c():
    x6=dpk_open.get()
    y6=dpk_close.get()
    z6=dpk_cash.get()
    d6=dpk_transfer.get()
    e6=dpk_pos.get()
    f6=dpk_expenses.get()
    dpk_pms = (dpk_price_txt.get())

    if x6=="" or y6=="" or  z6==""  or  d6==""  or  e6==""  or  f6==""  or dpk_pms=="":
        messagebox.showerror("","Input value")
    else:
        l7=round(float(y6)-float(x6),2)
        dpk_liter.config(text=f"{l7} L")
        a7=int(dpk_pms)
        b7=l7*a7
        dpk_amount.config(text=f"{round(b7)}")

        g6=int(z6)+int(d6)+int(e6)+int(f6)
        h6=g6-b7
        if g6 > b7:
            dpk_excess.config(text=round(h6))
            dpk_short.config(text="0.00")
            
        elif g6 < b7:
            dpk_short.config(text=round(h6))
            dpk_excess.config(text="0.00")

dpk_calc=Button(pump_dpk_frm,text="CALCULATE",font=("cambria",12,"bold"),fg="black",background="gray",borderwidth=0,justify='center',command=dpk_c)
dpk_calc.grid(row=11,column=0,padx=2,pady=2)

def dpk_cls():
    dpk_open.delete(0,END)
    dpk_close.delete(0,END)
    dpk_cash.delete(0,END)
    dpk_expenses.delete(0,END)
    dpk_pos.delete(0,END)
    dpk_transfer.delete(0,END)

dpk_calc=Button(pump_dpk_frm,text="CLEAR",font=("cambria",12,"bold"),fg="black",background="gray",borderwidth=0,justify='center',command=dpk_cls)
dpk_calc.grid(row=11,column=1,padx=2,pady=2)


# ___________________________________GAS______________________________________________________________________________________________________________
pump_gas_frm=LabelFrame(gas_screen,text="GAS",border=2,borderwidth=2,background="gray",font=("caligraphy",10,"bold"),fg="black")
pump_gas_frm.grid(row=0,column=3,padx=5,pady=2)

pump_gas_lbl=Label(pump_gas_frm,text='Opening',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_gas_lbl.grid(row=0,column=0)
gas_open=Entry(pump_gas_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
# pms_open.focus_set()
gas_open.grid(row=0,column=1)

pump_gas_lbl=Label(pump_gas_frm,text='Closing',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_gas_lbl.grid(row=1,column=0,pady=1)
gas_close=Entry(pump_gas_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
gas_close.grid(row=1,column=1,pady=1)

pump_gas_lbl=Label(pump_gas_frm,text='Liter Sold',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_gas_lbl.grid(row=2,column=0)
gas_liter=Label(pump_gas_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
gas_liter.grid(row=2,column=1)

pump_gas_lbl=Label(pump_gas_frm,text='Amount #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_gas_lbl.grid(row=3,column=0)
gas_amount=Label(pump_gas_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
gas_amount.grid(row=3,column=1)

pump_gas_lbl=Label(pump_gas_frm,text='Cash #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_gas_lbl.grid(row=4,column=0)
gas_cash=Entry(pump_gas_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
gas_cash.grid(row=4,column=1,pady=1)

pump_gas_lbl=Label(pump_gas_frm,text='Transfer #',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_gas_lbl.grid(row=5,column=0)
gas_transfer=Entry(pump_gas_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
gas_transfer.grid(row=5,column=1,pady=1)

pump_gas_lbl=Label(pump_gas_frm,text='P.O.S',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_gas_lbl.grid(row=6,column=0)
gas_pos=Entry(pump_gas_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
gas_pos.grid(row=6,column=1,pady=1)

pump_gas_lbl=Label(pump_gas_frm,text='Expenses',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_gas_lbl.grid(row=7,column=0)
gas_expenses=Entry(pump_gas_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
gas_expenses.grid(row=7,column=1,pady=1)

pump_gas_lbl=Label(pump_gas_frm,text='Excess',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_gas_lbl.grid(row=8,column=0)
gas_excess=Label(pump_gas_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
gas_excess.grid(row=8,column=1)

pump_gas_lbl=Label(pump_gas_frm,text='Shortage',font=("cambria",12,"bold","italic"),fg="black",background="gray")
pump_gas_lbl.grid(row=9,column=0)
gas_short=Label(pump_gas_frm,text='0.00',font=("cambria",12,"bold","italic"),fg="black",background="gray")
gas_short.grid(row=9,column=1)

gas_price_lbl=Label(pump_gas_frm,text='PRICE',font=("cambria",12,"bold","italic"),fg="black",background="gray")
gas_price_lbl.grid(row=10,column=0)
gas_price_txt=Entry(pump_gas_frm,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=0,justify='center')
gas_expenses.grid(row=10,column=1,pady=1)

#_________GAS_BUTTONs________
def gas_c():
    x7=gas_open.get()
    y7=gas_close.get()
    z7=gas_cash.get()
    d7=gas_transfer.get()
    e7=gas_pos.get()
    f7=gas_expenses.get()
    gas = (dpk_price_txt.get())

    if x7=="" or y7=="" or  z7==""  or  d7==""  or  e7==""  or  f7==""  or gas=="":
        messagebox.showerror("","Input value")
    else:
        l8=round(float(y7)-float(x7),2)
        gas_liter.config(text=f"{l8} L")
        a8=int(gas)
        b8=l8*a8
        gas_amount.config(text=f"{round(b8)}")

        g7=int(z7)+int(d7)+int(e7)+int(f7)
        h7=g7-b8
        if g7 > b8:
            gas_excess.config(text=round(h7))
            gas_short.config(text="0.00")
            
        elif g7 < b8:
            gas_short.config(text=round(h7))
            gas_excess.config(text="0.00")
            
gas_calc=Button(pump_gas_frm,text="CALCULATE",font=("cambria",12,"bold"),fg="black",background="gray",borderwidth=0,justify='center',command=gas_c)
gas_calc.grid(row=11,column=0,padx=2,pady=2)

def gas_cls():
    gas_open.delete(0,END)
    gas_close.delete(0,END)
    gas_cash.delete(0,END)
    gas_expenses.delete(0,END)
    gas_pos.delete(0,END)
    gas_transfer.delete(0,END)

gas_calc=Button(pump_gas_frm,text="CLEAR",font=("cambria",12,"bold"),fg="black",background="gray",borderwidth=0,justify='center',command=gas_cls)
gas_calc.grid(row=11,column=1,padx=2,pady=2)

#_______________________________general control pane______________________________________________________________________________________________________

#PRICE OBEJECTS
gen_price=Entry(ctrl3_screen,width=10,font=("cambria",10,"bold","italic"),fg="black",background="gray",borderwidth=1,justify='center')
gen_price.grid(row=0,column=0)
gen_price_lbl=Label(ctrl3_screen,text='PRICE',font=("cambria",12,"bold","italic"),fg="black",background="gray")
gen_price_lbl.grid(row=1,column=0)


#LITERS
t_liter_sold_lbl=Label(ctrl3_screen,text='',font=("cambria",12,"bold","italic"),fg="black",background="gray")
t_liter_sold_lbl.grid(row=0,column=1)
liter_sold_lbl=Label(ctrl3_screen,text='LITERS SOLD',font=("cambria",12,"bold","italic"),fg="black",background="gray")
liter_sold_lbl.grid(row=1,column=1)

#AMOUNT
t_liter_amount_lbl=Label(ctrl3_screen,text='',font=("cambria",12,"bold","italic"),fg="black",background="gray")
t_liter_amount_lbl.grid(row=0,column=2)
liter_amount_lbl=Label(ctrl3_screen,text='AMOUNT',font=("cambria",12,"bold","italic"),fg="black",background="gray")
liter_amount_lbl.grid(row=1,column=2)

#CASH
t_cash_lbl=Label(ctrl3_screen,text='',font=("cambria",12,"bold","italic"),fg="black",background="gray")
t_cash_lbl.grid(row=0,column=3)
liter_cash_lbl=Label(ctrl3_screen,text='CASH',font=("cambria",12,"bold","italic"),fg="black",background="gray")
liter_cash_lbl.grid(row=1,column=3)

#TRANSFER
t_transfer_lbl=Label(ctrl3_screen,text='',font=("cambria",12,"bold","italic"),fg="black",background="gray")
t_transfer_lbl.grid(row=0,column=4)
liter_transfer_lbl=Label(ctrl3_screen,text='TRANSFER',font=("cambria",12,"bold","italic"),fg="black",background="gray")
liter_transfer_lbl.grid(row=1,column=4)

#P.O.S
t_POS_lbl=Label(ctrl3_screen,text='',font=("cambria",12,"bold","italic"),fg="black",background="gray")
t_POS_lbl.grid(row=0,column=5)
liter_POS_lbl=Label(ctrl3_screen,text='P.O.S',font=("cambria",12,"bold","italic"),fg="black",background="gray")
liter_POS_lbl.grid(row=1,column=5)

#EXPENSES
t_expenses_lbl=Label(ctrl3_screen,text='',font=("cambria",12,"bold","italic"),fg="black",background="gray")
t_expenses_lbl.grid(row=0,column=6)
liter_expenses_lbl=Label(ctrl3_screen,text='EXPENSES',font=("cambria",12,"bold","italic"),fg="black",background="gray")
liter_expenses_lbl.grid(row=1,column=6)

# #EXCESS
# t_excess_lbl=Label(ctrl3_screen,text='',font=("cambria",12,"bold","italic"),fg="black",background="gray")
# t_excess_lbl.grid(row=0,column=7)
# liter_excess_lbl=Label(ctrl3_screen,text='EXCESS',font=("cambria",12,"bold","italic"),fg="black",background="gray")
# liter_excess_lbl.grid(row=1,column=7)


# #SHORTAGE
# t_shortage_lbl=Label(ctrl3_screen,text='',font=("cambria",12,"bold","italic"),fg="black",background="gray")
# t_shortage_lbl.grid(row=0,column=8)
# liter_shortage_lbl=Label(ctrl3_screen,text='SHORTAGE',font=("cambria",12,"bold","italic"),fg="black",background="gray")
# liter_shortage_lbl.grid(row=1,column=8)


# TOTAL
total_lbl=Label(ctrl3_screen,text='',font=("cambria",12,"bold","italic"),fg="black",background="gray")
total_lbl.grid(row=0,column=9)
gen_total_lbl=Label(ctrl3_screen,text='TOTAL',font=("cambria",12,"bold","italic"),fg="black",background="gray")
gen_total_lbl.grid(row=1,column=9)


#CALCULATE
def t_cal():

    p_pms = (gen_price.get())

    x1=pms2_open.get()
    y1=pms2_close.get()
    z1=pms2_cash.get()
    d1=pms2_transfer.get()
    e1=pms2_pos.get()
    f1=pms2_expenses.get()
    
    x2=pms3_open.get()
    y2=pms3_close.get()
    z2=pms3_cash.get()
    d2=pms3_transfer.get()
    e2=pms3_pos.get()
    f2=pms3_expenses.get()
    

    x3=pms4_open.get()
    y3=pms4_close.get()
    z3=pms4_cash.get()
    d3=pms4_transfer.get()
    e3=pms4_pos.get()
    f3=pms4_expenses.get()
    

    x4=pms5_open.get()
    y4=pms5_close.get()
    z4=pms5_cash.get()
    d4=pms5_transfer.get()
    e4=pms5_pos.get()
    f4=pms5_expenses.get()
    


    l2=round(float(y1)-float(x1),2)
    l3=round(float(y2)-float(x2),2)
    l4=round(float(y3)-float(x3),2)
    l5=round(float(y4)-float(x4),2)
    
    b2=round(l2*int(p_pms))
    b3=round(l3*int(p_pms))
    b4=round(l4*int(p_pms))
    b5=round(l5*int(p_pms))

    z1=int(pms2_cash.get())
    z2=int(pms3_cash.get())
    z3=int(pms4_cash.get())
    z4=int(pms5_cash.get())

    #Liters Sold
    t_liters=round(l2+l3+l4+l5,2)

    t_liter_sold_lbl.config(text=f"{t_liters} L")
    
    #amount sold
    t_amount=b2+b3+b4+b5
    t_liter_amount_lbl.config(text=f"#{t_amount}")

    #Cash
    t_cash=int(z1)+int(z2)+int(z3)+int(z4)
    t_cash_lbl.config(text=f"#{t_cash}")

    #Transfer
    t_transfer=int(d1)+int(d2)+int(d3)+int(d4)
    t_transfer_lbl.config(text=f"#{t_transfer}")

    #P.O.S
    t_pos=int(e1)+int(e2)+int(e3)+int(e4)
    t_POS_lbl.config(text=f"#{t_pos}")

    #EXPENSES
    t_exp=int(f1)+int(f2)+int(f3)+int(f4)
    t_expenses_lbl.config(text=f"{t_exp}")

    #Total
    t_total=t_cash+t_transfer+t_pos+t_exp
    total_lbl.config(text=f"#{t_total}")

    #SHORT
    # sht=t_total -  t_amount
    # if t_total < t_amount:
        
    #     t_shortage_lbl.config(text=f"#{sht}")
    #     t_excess_lbl.config(text="0.00")
    # elif t_total < t_amount:
        
    #     t_excess_lbl.config(text=f"#{sht}")
    #     t_shortage_lbl.config(text="0.00")
t_calc=Button(ctrl3_screen,text="COMPUTE",font=("cambria",12,"bold"),fg="green",background="gray",borderwidth=0,justify='center',command=t_cal)
t_calc.grid(row=0,column=10)

#CLEAR
def t_cls():
    pass
t_clear=Button(ctrl3_screen,text="CLEAR",font=("cambria",12,"bold"),fg="green",background="gray",borderwidth=0,justify='center',command=t_cls)
t_clear.grid(row=1,column=10)

#SAVE

def t_save():
    p_pms = (gen_price.get())

    x1=pms2_open.get()
    y1=pms2_close.get()
    z1=pms2_cash.get()
    d1=pms2_transfer.get()
    e1=pms2_pos.get()
    f1=pms2_expenses.get()
    
    x2=pms3_open.get()
    y2=pms3_close.get()
    z2=pms3_cash.get()
    d2=pms3_transfer.get()
    e2=pms3_pos.get()
    f2=pms3_expenses.get()
    

    x3=pms4_open.get()
    y3=pms4_close.get()
    z3=pms4_cash.get()
    d3=pms4_transfer.get()
    e3=pms4_pos.get()
    f3=pms4_expenses.get()
    

    x4=pms5_open.get()
    y4=pms5_close.get()
    z4=pms5_cash.get()
    d4=pms5_transfer.get()
    e4=pms5_pos.get()
    f4=pms5_expenses.get()
   
    l2=pms2_liter.cget("text")
    l3=pms3_liter.cget("text")
    l4=pms4_liter.cget("text")
    l5=pms5_liter.cget("text")
    
    b2=pms2_amount.cget("text")
    b3=pms3_amount.cget("text")
    b4=pms4_amount.cget("text")
    b5=pms5_amount.cget("text")

    z1=pms2_cash.get()
    z2=pms3_cash.get()
    z3=pms4_cash.get()
    z4=pms5_cash.get()
    
    t_l=t_liter_sold_lbl.cget("text")
    t_m=t_liter_amount_lbl.cget("text")
    t_c=t_cash_lbl.cget("text")
    t_t=t_transfer_lbl.cget("text")
    t_p=t_POS_lbl.cget("text")
    t_e=t_expenses_lbl.cget("text")
    t_x=total_lbl.cget("text")


    today=date.today()
    d_today=today.strftime("%d%m%Y")
    dte=today.strftime("%d / %m / %Y")
    pdf_file=filedialog.asksaveasfilename(initialdir="C:/Users/user/Desktop/",title="bisyloil",filetypes=(("PDF Files","*.pdf"),))
    
    
    pdf=FPDF('P','mm','A4')
    pdf.add_page()
    pdf.set_font('helvetica','B',10)

    pdf.cell(40,15,f'{dte}',ln=False)
    pdf.cell(40,15,f'PRICE:# {p_pms}',ln=True)
    #____________________pumps________________________________
    pdf.cell(40,5,'PUMP2',ln=False)
    pdf.cell(40,5,'PUMP3',ln=False)
    pdf.cell(40,5,'PUMP4',ln=False)
    pdf.cell(40,5,'PUMP5',ln=True)

    pdf.cell(40,5,f'opening:  {x1}',ln=False)
    pdf.cell(40,5,f'opening:  {x2}',ln=False)
    pdf.cell(40,5,f'opening:  {x3}',ln=False)
    pdf.cell(40,5,f'opening:  {x4}',ln=True)
    

    pdf.cell(40,5,f'closing:  {y1}',ln=False)
    pdf.cell(40,5,f'closing:  {y2}',ln=False)
    pdf.cell(40,5,f'closing:  {y3}',ln=False)
    pdf.cell(40,5,f'closing:  {y4}',ln=True)

    pdf.cell(40,5,f'liters:   {l2}',ln=False)
    pdf.cell(40,5,f'liters:   {l3}',ln=False)
    pdf.cell(40,5,f'liters:   {l4}',ln=False)
    pdf.cell(40,5,f'liters:   {l5}',ln=True)

    pdf.cell(40,5,f'amount:   {b2}',ln=False)
    pdf.cell(40,5,f'amount:   {b3}',ln=False)
    pdf.cell(40,5,f'amount:   {b4}',ln=False)
    pdf.cell(40,5,f'amount:   {b5}',ln=True)
    
    pdf.cell(40,5,f'cash:     {z1}',ln=False)
    pdf.cell(40,5,f'cash:     {z2}',ln=False)
    pdf.cell(40,5,f'cash:     {z3}',ln=False)
    pdf.cell(40,5,f'cash:     {z4}',ln=True)

    pdf.cell(40,5,f'transfer: {d1}',ln=False)
    pdf.cell(40,5,f'transfer: {d2}',ln=False)
    pdf.cell(40,5,f'transfer: {d3}',ln=False)
    pdf.cell(40,5,f'transfer: {d4}',ln=True)

    pdf.cell(40,5,f'pos:      {e1}',ln=False)
    pdf.cell(40,5,f'pos:      {e2}',ln=False)
    pdf.cell(40,5,f'pos:      {e3}',ln=False)
    pdf.cell(40,5,f'pos:      {e4}',ln=True)

    pdf.cell(40,5,f'expenses: {f1}',ln=False)
    pdf.cell(40,5,f'expenses: {f2}',ln=False)
    pdf.cell(40,5,f'expenses: {f3}',ln=False)
    pdf.cell(40,5,f'expenses: {f4}',ln=True)
#_________________gene________________________
    pdf.cell(40,10,f'TOTAL LITERS: {t_l}',ln=True)
    pdf.cell(40,5,f'AMOUNT: {t_m}',ln=True)
    pdf.cell(40,5,f'TOTAL CASH: {t_c}',ln=True)
    pdf.cell(40,5,f'TOTAL TRANSFER: {t_t}',ln=True)
    pdf.cell(40,5,f'TOTAL P.O.S: {t_p}',ln=True)
    pdf.cell(40,5,f'TOTAL EXPENSES: {t_e}',ln=True)
    pdf.cell(40,5,f'TOTAL: {t_x}',ln=True)


    #_____________________AGO_____________________________________

    pdf.cell(40,5,f'DIESEL',ln=True)
    pdf.cell(40,15,f'PRICE:# {deisel_price_txt.get()}',ln=True)
    
    pdf.cell(40,5,f'opening:# {deisel_open.get()}',ln=True)
    pdf.cell(40,5,f'closing:# {deisel_close.get()}',ln=True)
    pdf.cell(40,5,f'liters:# {deisel_liter.cget("text")}',ln=True)
    pdf.cell(40,5,f'amount:# {deisel_amount.cget("text")}',ln=True)
    pdf.cell(40,5,f'cash:# {deisel_cash.get()}',ln=True)
    pdf.cell(40,5,f'transfer:# {deisel_transfer.get()}',ln=True)
    pdf.cell(40,5,f'P.O.S:# {deisel_pos.get()}',ln=True)
    pdf.cell(40,5,f'Expenses:# {deisel_expenses.get()}',ln=True)
    
    pdf.output(f'{pdf_file},{d_today}.pdf')
    messagebox.showinfo("BISYL","SUCCESSFUL")
    pdf.close()
    
t_store=Button(ctrl3_screen,text="SAVE",font=("cambria",12,"bold"),fg="green",background="gray",borderwidth=0,justify='center',command=t_save)
t_store.grid(row=0,column=11)


#CLOSE
def t_close():
    pms_screen.pack_forget()
    deisel_screen.pack_forget()
    dpk_screen.pack_forget()
    gas_screen.pack_forget()

t_quit=Button(ctrl3_screen,text="CLOSE",font=("cambria",12,"bold"),fg="green",background="gray",borderwidth=0,justify='center',command=t_close)
t_quit.grid(row=1,column=11)

#_________________________________________________________________________control buttons_____________________________________________________________________

img2=PhotoImage(file=(resource_path("C:/Users/user/Desktop/PMS/img/logo.png")))

def pms_me():
    pms_screen.pack(padx=115,pady=60)
    deisel_screen.pack_forget()
    dpk_screen.pack_forget()
    gas_screen.pack_forget()

pms_btn=Button(ctrl1_screen,text="P.M.S",font=("elephant",10,"bold"),width=6,height=2,background="gray",foreground="green",command=pms_me)
pms_btn.pack()

lbl_nme=Label(ctrl1_screen,text="",image=img2,font=("helvetic",10,"bold"),background="gray",foreground="green")
lbl_nme.pack()

def ago():
    deisel_screen.pack(padx=395,pady=50)
    pms_screen.pack_forget()
    dpk_screen.pack_forget()
    gas_screen.pack_forget()

deisel_btn=Button(ctrl1_screen,text="A.G.O",font=("elephant",10,"bold"),width=6,height=2,background="gray",foreground="green",command=ago)
deisel_btn.pack()


def dpk():
    dpk_screen.pack(padx=395,pady=50)
    pms_screen.pack_forget()
    deisel_screen.pack_forget()
    gas_screen.pack_forget()

dpk_btn=Button(ctrl2_screen,text="D.P.K",font=("elephant",10,"bold"),width=6,height=2,background="gray",foreground="green",command=dpk)
dpk_btn.pack()

def xexit():
    home.destroy()
exit_btn=Button(ctrl2_screen,text="BISYL \n OIL \n & \n GAS",image=img2,font=("helvetic",10,"bold"),background="gray",foreground="green",borderwidth=0,command=xexit)
exit_btn.pack()

# lbl_nme=Label(ctrl2_screen,text="",image=img2,font=("helvetic",10,"bold"),background="gray",foreground="green")
# lbl_nme.pack()


def gas():
    gas_screen.pack(padx=395,pady=50)
    pms_screen.pack_forget()
    deisel_screen.pack_forget()
    dpk_screen.pack_forget()

gas_btn=Button(ctrl2_screen,text="GAS",font=("elephant",10,"bold"),width=6,height=2,background="gray",foreground="green",command=gas)
gas_btn.pack()

mainloop()
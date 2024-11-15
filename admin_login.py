# import os
# from tkinter import *
# from tkinter import PhotoImage
# from tkinter import messagebox,Message
# import sys

# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")

#     return os.path.join(base_path, relative_path)

# login=Tk()
# login.title('Petroleum Manangemnt System')
# login.iconbitmap(resource_path('img_logo.ico'))
# app_width = 150
# app_height = 95
# screen_width = login.winfo_screenwidth()
# screen_height = login.winfo_screenheight()
# x = (screen_width / 2) - (app_width / 2)
# y = (screen_height / 2) - (app_height / 2)
# login.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
# login.resizable(width=False, height=False)
# login.wm_overrideredirect(1)


# frm_login=LabelFrame(login,text="ADMIN",labelanchor='n',font=("cambria",14,"bold"),background="gray",foreground="green",width=200)
# frm_login.pack(ipadx=20)
# img=PhotoImage(file=resource_path("C:/Users/user/Desktop/PMS/nme.png"))
# lbl_img=Label(frm_login,image=img)
# lbl_img.place(relheight=1,relwidth=1)
# txt_psswd=Entry(frm_login,width=15,font=("cambria",10,"bold","italic"),fg="black",background="gray",show=" ",borderwidth=1,justify='center',)
# txt_psswd.grid(row=0,column=0,columnspan=2,padx=20,pady=5)
# txt_psswd.focus_set()
# def enter():
#     if txt_psswd.get()=="bisyl001":
#         messagebox.showinfo('BISYL OIL & GAS',"WELCOME!!!")
        
#         login.destroy()
        
#     else:
#         messagebox.showwarning("BISYL OIL & GAS","UNAUTHORISED USER")
#         txt_psswd.delete(0,END)
#         txt_psswd.focus_set()
# btn_enter=Button(frm_login,text="LOGIN",font=("cambria",10,"bold"),borderwidth=0,foreground="green",height=1,command=enter)
# btn_enter.grid(row=1,column=0,padx=2,pady=20)

# def sexit():
#     import my_home
#     my_home.home.destroy()
#     login.destroy()
    
# btn_close=Button(frm_login,text="EXIT",font=("cambria",10,"bold"),borderwidth=0,foreground="red",height=1,command=sexit)
# btn_close.grid(row=1,column=1,padx=2,pady=20)
# login.mainloop()
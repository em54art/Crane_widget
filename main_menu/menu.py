from tkinter import Label,Button,Text,HORIZONTAL
import customtkinter
from time import strftime
import calendar
from clock import popout_windowC
#-----------root-------
root = customtkinter.CTk()

root.title('Crane widget')
root.geometry("500x500")

#background colour
switch_mode = '#ffffff'
root.configure(fg_color=f'{switch_mode}')

#---------------------
#change background colour
switch_var = customtkinter.StringVar(value="on")
font_color = '#333333'

switch = None  # Declare switch as a global variable
def switch_event():
    global font_color, switch
    #grab color value
    get_var = switch_var.get()
    switch_mode = get_var
    #change background color
    root.configure(fg_color=f'{switch_mode}')
    if switch:
        font_color = changeFont(switch_mode)
        gui()

def changeFont(switch_mode):
    if switch_mode == '#ffffff':
        return'#333333'
    else:
        return'#ffffff'

#-------------GUI-------

def gui():
    global font_color, switch,labelText
    
    titleText = Label(root, text= 'Widget list',font=('arial',25))
    titleText.grid(row=0,column=1)
    
    labelText = Label(root, text='Clock widget',font=('arial',16))
    labelText.grid(row=1,column=1, padx=10, pady=2)
    
    #pop up
    button_clock1 = customtkinter.CTkButton(root,text="clock test popup",fg_color = "#333333",hover_color= "#a6a6a6",command=popout_windowC)
    button_clock1.grid(row=3,column=1, padx=40, pady=2, sticky='e')
    
    switch = customtkinter.CTkSwitch(root, text="CTkSwitch", command=switch_event,progress_color="#ffffff",
         variable=switch_var,onvalue="#333333", offvalue="#ffffff",text_color = f'{font_color}')
    
    switch.grid(row=0,column=0, padx=40, pady=2, sticky='e')

gui()
root.mainloop()

from tkinter import Label,Button,Text,HORIZONTAL
import customtkinter
from time import strftime
import tkinter as tk
def popout_windowC():
    
    popup = customtkinter.CTk()
    popup.wm_title("clock test")
    popup.overrideredirect(True)
    #popup.geometry("200x200")
    popup.tk_setPalette('black')
    popup.attributes('-transparentcolor', 'black')
    popup.wm_attributes("-topmost", 1)
    #drag and drop 
    
    #digital clock
    def label_text():
        size = 25
        labelText1 = Label(popup, text='Clock widget',font=('arial',size))
        labelText1.grid(row=0,column=0)        
        
        string1 = strftime('%H:%M:%S %p')
        labelText1.config(text=string1)
        labelText1.after(1000, label_text)
    
    entryt = customtkinter.CTkLabel(popup, text='Font Size',font=('arial',25), text_color='#333333')
    entryt.grid(row=0,column=1)
    
    entry = customtkinter.CTkEntry(popup, placeholder_text="CTkEntry", state='normal')
    entry.grid(row=1,column=1)
    
    def button_event():
        get_entry = entry.get()
        print(f'{get_entry}')
    
    entry_button=customtkinter.CTkButton(popup,text='print',fg_color='#333333',text_color='#ffffff',hover_color= '#d9d9d9' ,command=button_event)
    entry_button.grid(row=2,column=1)
    
    #func
    label_text()
    
    popup.mainloop()

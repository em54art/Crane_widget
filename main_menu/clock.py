from tkinter import Label,Button,Text,HORIZONTAL
import customtkinter
from time import strftime
import tkinter as tk
def popout_windowC():
    
    popup = customtkinter.CTk()
    popup.wm_title("clock test")
    popup.overrideredirect(True)
    popup.geometry("200x200")
    popup.tk_setPalette('black')
    popup.attributes('-transparentcolor', 'black')
    popup.wm_attributes("-topmost", 1)
    
    #drag and drop 
    
    def label_text():        
        labelText1 = Label(popup, text='Clock widget',font=('arial',25))
        labelText1.grid(row=0,column=0)        
        
        
        string1 = strftime('%H:%M:%S %p')
        labelText1.config(text=string1)
        labelText1.after(1000, label_text)

    
    label_text()
    
    popup.mainloop()

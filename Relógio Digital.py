from tkinter import *
import time

def mostrar_hora():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, mostrar_hora)

root = Tk()
root.title("Relógio Digital")

label = Label(root, font=("Arial", 80), bg="black", fg="white")
label.pack(padx=20, pady=20)

mostrar_hora()

root.mainloop()
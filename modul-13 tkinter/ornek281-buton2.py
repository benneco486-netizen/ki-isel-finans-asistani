import tkinter as tk
from tkinter import messagebox
pencere = tk.Tk()
pencere.title("buton örneği2")
pencere.geometry("600x450")

def buttonfonks():
    messagebox.showinfo("buton mesajı","turuncu butona tıklandı")
  

button=tk.Button(pencere,
               text="ben turuncu bir butonum",
               bg="orange",
               fg="black",
               activebackground="black",
               activeforeground="orange",
               font=20,
               height=2,
               width=20,
               cursor="hand2",
               command= buttonfonks)
button.pack()
pencere.mainloop()
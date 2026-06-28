import tkinter as tk
pencere = tk.Tk()
pencere.title("buton uygulaması")
pencere.geometry("600x450")

def buttonfonks():
  print("tutncu butona tıkladın")

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

               
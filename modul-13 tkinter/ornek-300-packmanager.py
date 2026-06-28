from tkinter import *
tk = Tk()
tk.title("Python Tkinter Eğitimi")
tk.geometry("600x450")

#Pack
P1 = Button(tk, text="Pack Button 1",fg="red")
P1.pack(side=LEFT)

P6 = Button(tk, text="Pack Button 6",fg="yellow")
P6.pack(side=RIGHT)

P2 = Button(tk, text="Pack Button 2",fg="blue")
P2.pack(side=LEFT)

P3 = Button(tk, text="Pack Button 3",fg="brown")
P3.pack(side=TOP)

P4 = Button(tk, text="Pack Button 4",fg="orange")
P4.pack(side=BOTTOM)

P5_buyuk= Button(tk, text="Pack Button 5",fg="pink",bg="gray")
P5_buyuk.pack(side=BOTTOM,fill=BOTH, expand=True)

tk.mainloop()
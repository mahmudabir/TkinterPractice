from tkinter import *


window = Tk()
window.geometry("300x300")
window.title("Welcome")

# label1 = Label(window, text="Welcome to tkinter", fg="blue", bg="yellow", relief="solid" ,font=("arial",12, "bold")).pack()
# label1 = Label(window, text="Welcome to tkinter", fg="blue", bg="yellow", relief="solid" ,font=("arial",12, "bold")).place(x=110,y=110)
label1 = Label(window, text="Welcome to tkinter", fg="blue", bg="yellow", relief="solid" ,font=("arial",12, "bold"))
# label1.pack(fill=BOTH, pady=2, padx=2, expand=True)
# label1.place(x=110,y=80)
# label1.grid(row=1,column=1)
label1.pack()

button1=Button(window, text="Demo", fg="white", bg="brown", relief=RIDGE,font=("arial",12, "bold")) # RIDGE, GROOV, SUNKEN, RAISED
button1.place(x=115,y=110)


window.mainloop()
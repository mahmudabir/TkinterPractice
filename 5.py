from tkinter import *
import tkinter.messagebox as messagebox
from PIL import Image
import PIL.ImageTk as ImageTk

root = Tk()
root.geometry("500x700")
root.title("Registration Form")

def exitt():
    exit()

def printt():
    fn=fname.get()
    ln=lname.get()
    date=dob.get()
    country=var.get()

    
    pl1=var_c1.get()
    pl2=var_c2.get()

    if pl1=="1":
        pl1="Java"
    else:
        pl1=""

    if pl2=="1":
        pl2="Python"
    else:
        pl2=""

    gender=var_r.get()

    print(f"Your name is {fn} {ln}")
    print(f"Your birth date is {date}")
    print(f"Your country is {country}")
    print(f"Your programming language: {pl1}, {pl2}")
    print(f"Your gender: {gender}")
    messagebox.showinfo("Wellcome", f"{fn}, You have successfully signed up!!!")

def about():
    messagebox.showinfo("About", "Hello There!!!!!!!!!!")

def another():
    window=Tk()
    window.title("Second Window")
    window.geometry("250x200")
    label_window=Label(window, text="Registration Complete", relief="solid", font=("arial", 12, 'bold')).place(x=30,y=70)
    button_window=Button(window, text="Exit", width=12, bg='brown', fg='white', command=exitt).place(x=80, y=110)

menu=Menu(root)
root.config(menu=menu)


# Menu
sub_menu1=Menu(menu)
menu.add_cascade(label="File", menu=sub_menu1)
sub_menu1.add_command(label="Exit", command=exitt)

sub_menu2=Menu(menu)
menu.add_cascade(label="Others", menu=sub_menu2)
sub_menu2.add_command(label="About", command=about)

# Image Input
img = Image.open('default.png')
img = img.resize((125,125), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)

lab = Label(image=photo)
lab.pack()


fname = StringVar()
lname = StringVar()
dob = StringVar()
var = StringVar()
var_c1 = StringVar()
var_c2 = StringVar()
var_r = StringVar()






# Lable
label_0 = Label(root, text="Registation Form", relief="solid", width=20, font=("arial", 19, "bold"))
label_0.place(x=90, y=150)

# Lable
label_1 = Label(root, text="First Name: ", relief="solid", width=10, font=("bold", 10))
label_1.place(x=80, y=240)

# text box
entry_1 = Entry(root, textvariable=fname)
entry_1.place(x=240, y=242)

# Lable
label_2 = Label(root, text="Last Name: ", relief="solid", width=10, font=("bold", 10))
label_2.place(x=80, y=280)

# text box
entry_2 = Entry(root, textvariable=lname)
entry_2.place(x=240, y=282)

# Lable
label_3 = Label(root, text="DOB: ", relief="solid", width=10, font=("bold", 10))
label_3.place(x=80, y=320)

# text box
entry_3 = Entry(root, textvariable=dob)
entry_3.place(x=240, y=322)

# Lable
label_3 = Label(root, text="Country: ", relief="solid", width=10, font=("bold", 10))
label_3.place(x=80, y=370)

# Drop down list
country_list = ['America', 'Bangladesh', 'Pakistan', 'China', 'Japan']
droplist = OptionMenu(root, var, *country_list)
var.set("Select Country")
droplist.config(width=15)
droplist.place(x=230, y=372)

# Lable
label_4 = Label(root, text="Prog. Lang.: ", relief="solid", width=10, font=("bold", 10))
label_4.place(x=80, y=412)


# Check box
c1=Checkbutton(root, text="Java", variable=var_c1).place(x=240, y=412)
c1=Checkbutton(root, text="Python", variable=var_c2).place(x=290, y=412)


# Lable
label_5 = Label(root, text="Gender: ", relief="solid", width=10, font=("bold", 10))
label_5.place(x=80, y=452)

# Radio Button
r1=Radiobutton(root, text="Male", variable=var_r, value="Male").place(x=240, y=452)
r2=Radiobutton(root, text="Female", variable=var_r, value="Female").place(x=290, y=452)


# Button
but_signup = Button(root, text="Sign Up", width=12, fg="white", bg="brown", command=printt)
but_signup.place(x=150,y=500)

# Button
but_exit = Button(root, text="Exit", width=12, fg="white", bg="brown", command=exitt)
but_exit.place(x=280,y=500)

# Button
but_another = Button(root, text="Another", width=12, fg="white", bg="brown", command=another)
but_another.place(x=208,y=560)













root.mainloop()

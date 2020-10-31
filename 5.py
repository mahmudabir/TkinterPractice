from tkinter import *
from PIL import Image
import PIL.ImageTk as ImageTk

root = Tk()
root.geometry("500x600")
root.title("Registration Form")


img = Image.open('default.png')
img = img.resize((125,125), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)

lab = Label(image=photo)
lab.pack()


fname=StringVar()
lname=StringVar()
dob=StringVar()
var=StringVar()




def exitt():
    exit()

def printt():
    fn=fname.get()
    ln=lname.get()
    date=dob.get()
    country=var.get()

    print(f"Your name is {fn} {ln}")
    print(f"Your birth date is {date}")
    print(f"Your country is {country}")


label_0 = Label(root, text="Registation Form", relief="solid", width=20, font=("arial", 19, "bold"))
label_0.place(x=90, y=150)


label_1 = Label(root, text="First Name: ", relief="solid", width=10, font=("bold", 10))
label_1.place(x=80, y=240)

entry_1 = Entry(root, textvariable=fname)
entry_1.place(x=240, y=242)


label_2 = Label(root, text="Last Name: ", relief="solid", width=10, font=("bold", 10))
label_2.place(x=80, y=280)

entry_2 = Entry(root, textvariable=lname)
entry_2.place(x=240, y=282)


label_3 = Label(root, text="DOB: ", relief="solid", width=10, font=("bold", 10))
label_3.place(x=80, y=320)

entry_3 = Entry(root, textvariable=dob)
entry_3.place(x=240, y=322)


label_3 = Label(root, text="Country: ", relief="solid", width=10, font=("bold", 10))
label_3.place(x=80, y=370)

country_list = ['America', 'Bangladesh', 'Pakistan', 'China', 'Japan']
droplist = OptionMenu(root, var, *country_list)
var.set("Select Country")
droplist.config(width=15)
droplist.place(x=230, y=372)




but_signup = Button(root, text="Sign Up", width=12, fg="white", bg="brown", command=printt)
but_signup.place(x=150,y=450)


but_exit = Button(root, text="Exit", width=12, fg="white", bg="brown", command=exitt)
but_exit.place(x=280,y=450)











root.mainloop()

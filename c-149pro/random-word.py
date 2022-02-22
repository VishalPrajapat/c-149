from tkinter import *
import random

root=Tk()
root.title(" Random Word ")
root.geometry("400x400")
root.configure(background="yellow")
label_randword=Label(root)
list1=["hdjh","gcdgvd","gdjvdjhd","vvdvdhhd","hvdvhdvhdvd","vdvhdhdhv","svshdhvdhd","vaid13e","bgdhshhd"]
print(list1)

def randomno():
    randomno1=random.randint(0,8)
    randomno1=list1[randomno1]
    label_randword["text"]=str(randomno1)
       
btn=Button(root, text="Generate A random ",command=randomno)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label_randword.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()

from tkinter import *
import random


root=Tk()
root.title("password generator")
#root.geometry("700x500")

def press():
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
    's','','u','v','w','x','y','z','A','B','C','D','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    number=['1','2','3','4','5','6','7','8','9','0']
    symbol=['!',"@",'#','$','%','^','&','*','(',')','+']
    
    password=[]
    
    for char in range(1,int(e1.get()) +1):
        random_choice=random.choice(letters)
        password+=random_choice
    for num in range(1,int(e2.get()) +1):

        random_number_choice=random.choice(number)
        password+=random_number_choice
    for num in range(1,int(e3.get()) +1):
        random_number_choice=random.choice(symbol)
        password+=random_number_choice
    random.shuffle(password)
    str1 = ''.join(password)
    l=Label(root,text=f"THE PASSWORD IS:{str1}",font=("Arial",15,"bold"))
    l.grid(row=6,column=0)

lbl=Label(root,text='WELCOME TO PASSWORD GENERATOR!!',
font=('Arial',48,'bold'),
fg='white',
bg='black',
relief=RAISED,
bd=20,
padx=10,
pady=10).grid(row=0,column=0)

lbl2=Label(root,text="HOW MANY LETTER DO YOU WANT IN YOUR PASSWORD:",
font=("Arial",15,"bold"))
lbl2.grid(row=2,column=0,sticky=W)

e1=Entry(root,width=35,borderwidth=5)
e1.grid(row=2,column=0,padx=10,pady=10)

lbl2=Label(root,text="HOW MANY NUMBER DO YOU WANT IN YOUR PASSWORD:",
font=("Arial",15,"bold"))
lbl2.grid(row=3,column=0,sticky=W)

e2=Entry(root,width=35,borderwidth=5)
e2.grid(row=3,column=0,padx=10,pady=10)
lbl2=Label(root,text="HOW MANY SYMBOL DO YOU WANT IN YOUR PASSWORD:",
font=("Arial",15,"bold"))
lbl2.grid(row=4,column=0,sticky=W)

e3=Entry(root,width=35,borderwidth=5)
e3.grid(row=4,column=0,padx=10,pady=10)


lbl2=Label(root,text="GENERATE PASSWORD",
font=("Arial",40,"bold"))
lbl2.grid(row=5,column=0,sticky=W)

BTN=Button(root,text="press",padx=20,pady=10,bd=20,fg="green",bg="black",command=press).grid(row=5,column=0)






root.mainloop()

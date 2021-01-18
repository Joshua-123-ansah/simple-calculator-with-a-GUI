from tkinter import *

window=Tk()
window.title("Simple Calculator")
e=Entry(window,bg="#B8B8B8",borderwidth=5,width=35)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(num):
    e.insert(END,num)
    
def sign_operation(sign):
    global sign_
    sign_=sign
    global first_number
    current=e.get()
    first_number=int(current)
    clear()

def equalsign():
  second_number=e.get()
  clear()
  if sign_=="+":
    e.insert(0,first_number+int(second_number))
  elif sign_=="-":
      e.insert(0,first_number-int(second_number))
  elif sign_=="*":
      e.insert(0,first_number*int(second_number))
  elif sign_=="/":
      e.insert(0,first_number/int(second_number))
    
  

def clear():
    e.delete(0,END)
   
###############Buttons#############
b1=Button(window,text="1",padx=40,pady=20,command=lambda:button_click(1))
b2=Button(window,text="2",padx=40,pady=20,command=lambda:button_click(2))
b3=Button(window,text="3",padx=40,pady=20,command=lambda:button_click(3))
b4=Button(window,text="4",padx=40,pady=20,command=lambda:button_click(4))
b5=Button(window,text="5",padx=40,pady=20,command=lambda:button_click(5))
b6=Button(window,text="6",padx=40,pady=20,command=lambda:button_click(6))
b7=Button(window,text="7",padx=40,pady=20,command=lambda:button_click(7))
b8=Button(window,text="8",padx=40,pady=20,command=lambda:button_click(8))
b9=Button(window,text="9",padx=40,pady=20,command=lambda:button_click(9))
b0=Button(window,text="0",padx=40,pady=20,command=lambda:button_click(0))

clear_sign=Button(window,text="Clear",padx=78,pady=20,command=clear)
plus_sign=Button(window,text="+",padx=40,pady=20,command=lambda:sign_operation("+"))
equal_sign=Button(window,text="=",padx=87,pady=20,command=equalsign)

substraction_sign=Button(window,text="-",padx=40,pady=20,command=lambda:sign_operation("-"))
multiplication_sign=Button(window,text="*",padx=40,pady=20,command=lambda:sign_operation("*"))
division_sign=Button(window,text="/",padx=40,pady=20,command=lambda:sign_operation("/"))

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

b0.grid(row=4,column=0)
clear_sign.grid(row=4,column=1,columnspan=2)

plus_sign.grid(row=5,column=0)
equal_sign.grid(row=5,column=1,columnspan=2)

substraction_sign.grid(row=6,column=0)
multiplication_sign.grid(row=6,column=1)
division_sign.grid(row=6,column=2)

window.mainloop()
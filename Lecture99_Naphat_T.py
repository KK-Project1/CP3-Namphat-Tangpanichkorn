from  tkinter import *
import math

def leftClickButton(event):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2))
    labelResult.configure(text=(f"BMI = {float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2)}"))
    Check = float(textBoxWeight.get()) / math.pow(float(textBoxHight.get()) / 100, 2)
    if Check <= 18.5:
        a = "ผอมเกิน"
    elif Check <= 22.9:
        a = "ปกติ"
    elif Check <= 24.9:
        a = "น้ำหนักเกิน"
    elif Check <= 29.9:
        a = "อ้วน"
    elif Check >= 30:
        a = "อ้วนเกินไป"
    labelResultCheck.configure(text=f"อยู่ในเกณฑ์: {a}")
    checktest()

def checktest():
    Check = float(textBoxWeight.get()) / math.pow(float(textBoxHight.get()) / 100, 2)
    if Check <= 18.5:
        a = "ผอมเกิน"
        print(a)
    elif Check <= 22.9:
        b = "ปกติ"
        print(b)
    elif Check <= 24.9:
        c = "น้ำหนักเกิน"
        print(c)
    elif Check <= 29.9:
        d = "อ้วน"
        print(d)
    elif Check >= 30:
        e = "อ้วนเกินไป"
        print(e)

mainWindow = Tk()
labelHight = Label(mainWindow,text="ส่วนสูง(Cm.)",font=("Hight",15))
labelHight.grid(row=0,column=0)
textBoxHight = Entry(mainWindow)
textBoxHight.grid(row=0,column=1)
labelWeight = Label(mainWindow,text="น้ำหนัก(Kg.)",font=("Hight",15))
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1,column=1)
calculatateButton = Button(mainWindow,text="คำนวน")
calculatateButton.bind('<Button-1>',leftClickButton)
calculatateButton.grid(row=2,column=0)
labelResult = Label(mainWindow,text="BMI = ?",font=("Hight",15))
labelResult.grid(row=2,column=1)
labelResultCheck = Label(mainWindow, text="รอผล", font=("Hight",15))
labelResultCheck.grid(row=3,column=1)
mainWindow.mainloop()
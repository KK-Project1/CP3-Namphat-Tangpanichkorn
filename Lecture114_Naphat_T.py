from forex_python.converter import CurrencyRates
from tkinter import *
from tkinter import ttk

c = CurrencyRates()
selectmoney = ['THB','USD','GBP','HKD','IDR','ILS','DKK','INR','CHF','EUR','CNY','SGD','MYR']

def leftClickButton(event):
    c = CurrencyRates()
    convertrate = float(input_money.get()) * c.get_rate(selectmoney1.get(),selectmoney2.get())
    labelResult.configure(text=str(round(convertrate, 3)))

mainWindow = Tk(className=' ')
labelText = Label(mainWindow,bg='gray',text="หาค่าเงินต่างประเทศ",font=("Hight",15))
labelText.place(x=200, y=15, anchor=CENTER)

#Selectmoney
labelMoney1 = Label(mainWindow,text='เลือกค่าเงิน',bg='gray',font=("Hight",10))
labelMoney1.place(x=100, y=55, anchor=CENTER)
selectmoney1 = ttk.Combobox(mainWindow,value=selectmoney,width=10)
selectmoney1.place(x=100, y=75, anchor=CENTER)
labelMoney2 = Label(mainWindow,text='เลือกค่าเงิน',bg='gray',font=("Hight",10))
labelMoney2.place(x=280, y=55, anchor=CENTER)
selectmoney2 = ttk.Combobox(mainWindow,value=selectmoney,width=10)
selectmoney2.place(x=280, y=75, anchor=CENTER)
labelMoney = Label(mainWindow,text='จำนวนเงิน',bg='gray',font=("Hight",10))
labelMoney.place(x=190, y=100, anchor=CENTER)
input_money = Entry(mainWindow,width=15)
input_money.place(x=190, y=120, anchor=CENTER)
#Selectmoney

#Button
Button = Button(mainWindow,text="แปลงค่าเงิน")
Button.bind('<Button-1>',leftClickButton)
Button.place(x=190, y=150, anchor=CENTER)
#Button

#Result
labelResult = Label(mainWindow,text="รอผล",font=("Hight",14))
labelResult.place(x=190, y=200, anchor=CENTER)
#Result

mainWindow.geometry("400x250")
mainWindow.configure(bg='gray')
mainWindow.mainloop()



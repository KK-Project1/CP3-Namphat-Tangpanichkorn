menuList = []
priceList = []

#-------------------funtion----------------------------

def showBill():
    print("------ My Food -----")
    for number in range(len(menuList)):
        print(f"{menuList[number]} ราคา {priceList[number]}")
    print("--------------------")
def priceAll():
    pricea = 0
    for price in priceList:
        pricea = pricea + int(price)
    print("ราคารวม :", pricea, "บาท")

# -------------------funtion----------------------------

while True:
    menuName = input("Please Enter Menu: ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price: "))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
priceAll()

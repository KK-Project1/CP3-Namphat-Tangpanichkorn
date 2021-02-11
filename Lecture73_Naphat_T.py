systemMenu = {"ข้าวหมกไก่":45,"ข้าวมันไก่":40,"ข้าวมันไก่ผสม":50,"ข้าวมันไก่พิเศษ":45}
menuList = []

def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])

def totalPrice():
    total = 0
    print("-----------------")
    for i in systemMenu.values():
        total = total + i
    print(f"Total: {total}")

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

showBill()
totalPrice()
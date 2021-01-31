def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True, showMenu()

    else:
        return False

def wrong():
    print("เข้าสู่ระบบไม่สำเร็จ")
    return  login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    set = userSelected
    if set == 1:
        price = int(input("Price: "))
        print(vatCalculator(price))
    elif set == 2:
        return priceCalculator()
    return userSelected, set


def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

login()


userInput = input("Username: ")
passInput = input("Password: ")
if userInput == "admin" and passInput == "admin" :
    print("Done!")
    print("------------")
    print("Welcome To Shop")
    print("----Menu----")
    print("1. ขนมปัง")
    print("2. น้ำ")
    print("3. โค้ก")
    print("4. ขนม")
    print("5. ไก่ทอด")
    print("------------")
    UserSet = int(input("เลือก Menu: "))
    if UserSet == 1:
        a = int(input("จำนวน: "))
        a2 = 15
        print(f"ซื้อขนมปังจำนวน: {a} ราคารวม: {a * a2}")
    elif UserSet == 2:
        b = int(input("จำนวน: "))
        b2 = 15
        print(f"ซื้อขนมปังจำนวน: {b} ราคารวม: {b * b2}")
    elif UserSet == 3:
        c = int(input("จำนวน: "))
        c2 = 15
        print(f"ซื้อขนมปังจำนวน: {c} ราคารวม: {c * c2}")
    elif UserSet == 4:
        d = int(input("จำนวน: "))
        d2 = 15
        print(f"ซื้อขนมปังจำนวน: {d} ราคารวม: {d * d2}")
    elif UserSet == 5:
        e = int(input("จำนวน: "))
        e2 = 15
        print(f"ซื้อขนมปังจำนวน: {e} ราคารวม: {e * e2}")
else: print("รหัสไม่ถูกต้อง")


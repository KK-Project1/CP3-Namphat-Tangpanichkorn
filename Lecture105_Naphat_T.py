class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turonAir(self):
        print("Turn On : Air")

class Car(Vehicle):
    pass
class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass

car1 = Car()
car1.turonAir()
pickup1 = PickUp()
pickup1.turonAir()
van1 = Van()
van1.turonAir()
estatecar1 = EstateCar()
estatecar1.turonAir()



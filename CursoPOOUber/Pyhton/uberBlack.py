from car import Car

class UberBlack(Car):
    typeCarAccepted = [] #Declarando los atributos de la clase uberblack
    seatsMaterial = []

    def __init__(self, license, driver, typeCarAccepted, seatsMaterial):
        super.__init__(license,driver) #Linea de la herenciade car.py
        self.typeCarAccepted= typeCarAccepted #Atributos de la clase uberpool
        self.seatsMaterial= seatsMaterial

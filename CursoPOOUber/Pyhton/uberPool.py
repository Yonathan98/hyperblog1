from car import Car

class UberPool(Car):
    brand = str
    model = str

    def __init__(self, license, driver, brand, model):
        super.__init__(license,driver) #Linea de la herenciade car.py
        self.brand= brand #Atributos de la clase uberpool
        self.model= model

class Car:
    id = int
    license = str
    driver = str
    passegenger = int
    def __init__ (self,license, driver): #constructor
        self.license = license
        self.driver = driver
    
    def setPassenger(self,passegengerNum): #Funcion para tener en cuenta el numero de pasajeros
        if passegengerNum >=4:
            self.__passenger = int(passegengerNum)
            print("Pasajeros asignados: "+ str(self.__passenger))
        else:
            print ("El número de pasajeros es demasiado bajo para esta categoria")
    
    def getPassenger(self): #Funcion cuando los pasajeros son diferentes de 4
        if self.__passenger != int:
            print(self.__passenger)
   
from car import Car #Traer la clase
from uberX import UberX
from account import Account
if __name__ == "__main__":
    print ("hola mundo")
    uberX = UberX("Ams234", Account ("Andres Herrera", "ANDA876"), "Chevrolet", "Sonic")
    print(vars(uberX)) #Traer todos los atributos de alguna clase al main
    print(vars(uberX.driver))

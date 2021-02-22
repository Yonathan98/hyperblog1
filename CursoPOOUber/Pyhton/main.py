from car import Car #Traer la clase
from account import Account
if __name__ == "__main__":
    print ("hola mundo")
    car = Car("Ams234", Account ("Andres Herrera", "ANDA876"))
    print(vars(car)) #Traer todos los atributos de car al main
    print(vars(car.driver))

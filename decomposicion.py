class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'En reposo'
        self._motor = Motor(cilindros=4) #esto es una variable privada
        self._seguridad = Airbag()

    def acelerar (self, tipo= 'despacio'):
        if tipo == "rapida":
            self._motor.inyecta_gasolina(10)
            self._motor.temperatura(12)
        else:
            self._motor.inyecta_gasolina(3)
            self._motor.temperatura(7)
        self._estado = 'en movimiento'
    def desAcelerar (self, tipo):
        if tipo == "brusca":
            self._seguridad.activar()
        else: 
            pass

class Motor:
    def __init__(self, cilindros, tipo = 'gasolina', nivelGasolina = 46000, temperatura = 0):#tipo es un parametro ya definido, se le llama default keyword, se entiende comoo un parametro por defecto.
        self.cilindros = cilindros
        self.tipo = tipo
        self.nivelGasolina = nivelGasolina
        self.estadoTemperatura = temperatura

    def inyecta_gasolina(self, cantidadGasolina):
        self.nivelGasolina = self.nivelGasolina - cantidadGasolina
    def temperatura(self, grados):
        self.estadoTemperatura = self.estadoTemperatura + grados
    def informacion (self): #revisar que todo esta bien
        print("\n")
        print(f"nivelGasolina = {self.nivelGasolina} y temperatura = {self.estadoTemperatura}")
        print("\n")
class Airbag:
    def __init__(self, estado = "optimo"):
        self.estado = estado
    def activar (self):
        print ("SISTEMA DE SEGURIDAD DE CHOQUES ACTIVADO")
        self.estado = "inhabilitado"

if __name__== "__main__":
    car1 = Automovil ("AAF", "Toyota", "Rojo")
    car1._motor.informacion()
    car1.acelerar("lenta")
    car1._motor.informacion()
    car1.desAcelerar("Brusca")

print("\n\n")





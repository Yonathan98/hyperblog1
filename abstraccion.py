# Creamos la clase Lavadora
class Lavadora:
    def __init__(self):
        pass
 # Tiene un método publico lavar que referencia a otros métodos
    def lavar(self, temperatura='Caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()
        
        # Los métodos privados de la clase no son relevantes
        # para el uso desde afuera de la clase y por
        # convención se inicia con _
    def _llenar_tanque_de_agua (self, temperatura):#metodo privado
        print(f'Llenando el tanque con agua {temperatura}')
    def _anadir_jabon(self):#metodo privado
        print('Añadiendo un jabon')
    def _lavar(self): #metodo privado
        print("Lavando la ropa")
    def _centrifugar(self):
        print("Centrifugando la ropa")
if __name__ == "__main__":
    lavadora = Lavadora()
    lavadora.lavar()
    



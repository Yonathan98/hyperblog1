class Millas:
    def __init__(self):
        self._distancia = 0

    # Función para obtener el valor de _distancia
    # Usando el decorador property
    # Llamamos a este setter haciendo avion.distancia = 20
    @property
    def distancia(self):
        print("Llamada al método getter")
        return self._distancia

    # Función para definir el valor de _distancia
    # Llamamos a esta función simplemente llamando a avion.distancia
    @distancia.setter
    def distancia(self, valor):
        if valor < 0:
            raise ValueError("No es posible convertir distancias menores a 0.")
        print("Llamada al método setter")
        self._distancia = valor

    # Función para eliminar el valor de _distancia
    # Llamamos a esta función llamando a del avion.distancia
    @distancia.deleter
    def distancia(self):
        print("Llamada al método deleter")
        del self._distancia
        
# Creamos un nuevo objeto 
avion = Millas()

# Indicamos la distancia
avion.distancia = 20

# Obtenemos su atributo distancia
print(avion.distancia)

# Eliminamos el atributo
del avion.distancia

# Salida
#Llamada al método setter
#Llamada al método getter
#20
#Llamada al método deleter
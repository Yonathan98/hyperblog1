class Coordenada: #definiendo la clase
    def __init__(self,x,y): #metodo constructor
        self.x = x
        self.y = y
    def distancia (self,otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2 #Diferencia entra las dos coordenadas
        y_diff = (self.y - otra_coordenada.y)**2

        return(x_diff + y_diff)**0.5

if __name__ == "__main__":
    coord_1 = Coordenada(3,30) #valores aleatorios de coordenadas
    coord_2 = Coordenada(4,8)

    #print(coord_1.distancia(coord_2)) #imprimiendo la diferencias de las dos coordenadas ingresadas
    print(isinstance(3, Coordenada))
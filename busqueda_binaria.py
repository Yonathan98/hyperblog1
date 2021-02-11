def busqueda_binaria (objetivo):
    epsilon = 0.01 #Aproximacion que se quiere llegar 
    bajo = 0.0
    alto = max(1.0, objetivo) #funcion que entrega el maximo numero
    respuesta = (alto + bajo) / 2
  
    if abs(respuesta**2 - objetivo) >= epsilon:
        print (f'bajo = {bajo}, alto= {alto}, respuesta= {respuesta}')
        if respuesta **2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
            respuesta = (alto + bajo) / 2
    print(f'La raiz cuadrada del objetivo es la {respuesta}')

def run():
    objetivo = int(input("Escoge un número: "))
    busqueda_binaria (objetivo)
if __name__ == '__main__':
    run()   
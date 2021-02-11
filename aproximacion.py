def aproximacion (objetivo):

    epsilon = 0.01 #Aproximacion que se quiere llegar 
    paso = epsilon**2
    respuesta= 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print (abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f"No se encontro la raiz cuadrada del {objetivo}")
    else:
        print(f"No se encontro la raiz cuadrada del {objetivo} es la {respuesta}")
objetivo = int(input("Escoge un número: "))
aproximacion(objetivo)
import random
def busqueda_lineal(lista, objetivo,iteraciones=0):
    match = False

    for elemento in lista: # 0(n)
        iteraciones += 1
        if elemento == objetivo:
            match = True
            break
    return (match, iteraciones)

if __name__ == "__main__":
    tamano_de_lista = int(input("De que tamaño sera la lista? "))
    objetivo = int(input("Que numero quieres encontrar? "))

    lista = [random.randint(0,100) for i in range (tamano_de_lista)]
    
    (encontrado,iteraciones) = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Iteraciones busqueda lineal: {iteraciones}')
    
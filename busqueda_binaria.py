import random
def busqueda_binaria(lista, comienzo, final, objetivo, iteraciones=0):
    print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final-1]}') #la busqueda que esta realizando
    iteraciones += 1 
    if comienzo > final:
        return (False, iteraciones)
    medio= (comienzo + final) // 2 #division de enteros

    if lista[medio] == objetivo :
        return (True, iteraciones)
    elif lista [medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, iteraciones=iteraciones) #busca en la lista hacia el final
    else:
        return busqueda_binaria(lista, comienzo, medio -1, objetivo, iteraciones=iteraciones) #busca en la lista hacia el principio
    
if __name__ == "__main__":
    tamano_de_lista = int(input("De que tamaño sera la lista? "))
    objetivo = int(input("Que numero quieres encontrar? "))

    lista = sorted([random.randint(0,100) for i in range (tamano_de_lista)]) #ordenar la lista
    
    
    (encontrado, iteraciones) = busqueda_binaria(lista,0,len(lista), objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Iteraciones busqueda binaria: {iteraciones}')
    
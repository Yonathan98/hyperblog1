#def run(num, rept):
 #   if num <= rept:
  #      cont = num
   #     print(str(2 ** cont) )
    #    run(num+1, rept)
    #else:
     #   print("Fin!")

#if __name__ == "__main__":
   # repeticiones = int(input("Cuantas potencias: "))
    #run(0, repeticiones)
def run():
    #limite = 1000
    #contador = 0
    #potencia_2= 2**contador
    #while potencia_2 < limite:
       # print("2 elevedo a " + str(contador) + "es igual a" + str(potencia_2)) 
        #contador = contador + 1
        #potencia_2= 2**contador
    limite=100 
    contador=0
    while contador < limite:
        print(contador)
        contador= contador+1
        if contador == 20:
            continue #aqui se pone break o continue



if __name__ == '__main__':
    run()
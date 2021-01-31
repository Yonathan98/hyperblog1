dolares = input ("¿Cuantos dolares tiene?: ")
dolares = float(dolares)
valor_pesos = 3569.01
pesos = dolares * valor_pesos
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos colombianos")
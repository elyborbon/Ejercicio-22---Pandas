import pandas as pd

lista = list(range(10,20))
print (lista)

pf = pd.Series(lista)

print(pf)

print(pf.nbytes)

lista_1 = pd.Series(list(range(30,41)))
print (lista_1)

lista_2 = pd.Series(list(range(30,0, -2)))
print (lista_2)
#suma
print (lista_1.add(lista_2))
#resta
print (lista_1.subtract(lista_2))
#multiplicacion
print (lista_1.multiply(lista_2))
#division
print (lista_1.divide(lista_2))
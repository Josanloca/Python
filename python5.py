import random

valor = (random.randint(1,10)*random.randint(1,10))

Res = input("Dime cual crees que es el numero: ")

if valor == int(Res):
    print("Correcto, "+str(valor)+" era el resultado")
else:
    print("Te equivocaste, el resultado era "+str(valor))


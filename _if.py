from traceback import print_tb


if True:
    print("deberia ejecutarse")

if False:
    print("nunca se ejecutara")

pet = input("Cual es tu mascota favorita? ")

if pet == "Perro":
    print("Genial")

elif pet == "Gato":
    print("Super")

elif pet == "Pez":
    print("Fantastico")

else:
    print("Adopta una moscota")


stock = int(input("Digita el stock => "))

if stock >= 100 and stock <= 1000:
    print("Correcto")
else:
    print("Incorrecto")


#Reto programa que verifique si un número e impar o par

numero = int (input("ingresa un nuumero:" ))

if numero %2 == 0:
    print("Numero par")

else:
    print("Número Impar") 

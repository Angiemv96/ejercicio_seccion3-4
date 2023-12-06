"""
Cree un programa que reciba dos números y muestre el mayor. 
En caso de que los números sean iguales
también se debe mostrar al usuario.
Autor: Angie Martinez
Fecha: 5 / Noviembre / 2023

"""

numero1 = int(input("Ingrese el primer mumero: "))
numero2 = int(input("Ingrese el segundo mumero: "))
if numero1 > numero2:
    print (str(numero1) + " Es mayor")
elif numero2>numero1:
    print(str(numero2) + " Es mayor")
else:
    print("Son iguales")






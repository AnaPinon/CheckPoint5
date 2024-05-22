# 1.	Crea un bucle for que imprima los números del 1 al 10.
for i in range(1,11):
    print (i)

#2.	Crea una función llamada suma que tome tres argumentos y devuelva la suma de los tres.
def suma(a,b,c):
    return a+b+c

resultado=suma(2,4,6)   
print(resultado)

#3.	Crea una función lambda con la misma funcionalidad que la función suma del ejercicio anterior.

resultado=lambda a,b,c : a+b+c
print (suma(2,4,6))

#4
nombre = "Enrique"
lista_nombres = ["Jessica", "Paul", "George", "Henry", "Adán"]

if nombre in lista_nombres:
    print(f"{nombre} se encuentra en la lista.")
else:
    print(f"{nombre} no se encuentra en la lista.")
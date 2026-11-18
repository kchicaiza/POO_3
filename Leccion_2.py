#Ejercicio 1
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(len(a & b))

#Ejercicio 2
datos = (10, 20, 30)
## datos[1] = 99
print(datos) # SAlE UN TYPE ERROR PORQUE LAS TUPLAS SON INMUTABLES

#Ejercicio 3
ciudad = "Paute y"
print(ciudad[-1].upper())

#Ejercicio 4
print(type(10.0))

#Ejercicio 5
frase = "aprendo Python en TEC"
print(len(frase.split()))

#Ejercicio 6
for i in range(3, 0, -1):
    print(i, end=" ")
print()

#Ejercicio 7
for x in [2, 4, 6]:
    if x == 7:
        print("Encontrado")
        break
else:
    print("No encontrado")

#Ejercicio 8
for n in [1, 2, 3, 4]:
    if n == 3:
        break
    print(n, end=" ")
print()

#Ejercicio 9
print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])

#Ejercicio 10
for i in range(1, 10, 3):
    print(i, end=" ")
print()

#Ejercicio 11
notas = [8.5, 6.0, 9.75, 4.5, 7.0, 10.0, 5.25]
cantidad = len(notas)
ordenar = sorted(notas)
nota_alta = ordenar[-1]
nota_baja = ordenar[0]
suma = 0
aprobados = 0
print(f"Nota mas alta: {nota_alta}")
print(f"Nota mas baja: {nota_baja}")
for i in notas:
    suma = suma + i
    if i >= 7:
       aprobados = aprobados + 1     
promedio = suma / cantidad
print(f"El promedio es: {promedio:.2f}")
print(f"Cantidad de aprobados es: {aprobados}")


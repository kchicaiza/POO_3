#Menu de Usuario
def pregunta1(a, b):
    return (len(a & b))

def pregunta2(*datos):
    #datos[1] = 99  
    return "TypeError ya que las tuplas son inmutables"

def pregunta3(ciudad):
    return ciudad[-1].upper()

def pregunta4():
    return type(10.0)

def pregunta5(frase):
    return len(frase.split())

def pregunta6(lista):
    for i in lista:
        print(i, end=" ")

def pregunta7(lista):
    for x in lista:
        if x == 7:
            print("Encontrado")
            break
    else:
        print("No encontrado")

def pregunta8(lista):
    for n in lista:
        if n == 3:
            break
        print(n, end=" ")

def pregunta9(lista):
    return [n ** 2 for n in lista if n % 2 == 0]

def pregunta10(lista):
    for i in lista:
        print(i, end=" ")

def pregunta11(lista):
    cantidad = len(lista)
    ordenar = sorted(lista)
    nota_alta = ordenar[-1]
    nota_baja = ordenar[0]
    suma = 0
    aprobados = 0
    print(f"Nota mas alta: {nota_alta}")
    print(f"Nota mas baja: {nota_baja}")
    for i in lista:
        suma = suma + i
        if  i>=7:
            aprobados = aprobados + 1
    promedio = suma / cantidad
    print(f"El promedio es: {promedio:.2f}")
    print(f"Cantidad de aprobados es: {aprobados}")
    
while True:
    print("****MENU USUARIOS****")
    print("1. INGRESAR NOMBRE")
    print("2. PREGUNTAS")
    print("3. SALIR")
    opcion = int(input("Ingrese una opcion: "))
    if opcion ==  1:
        nombre = input("Ingrese su nombre: ")
        print(f"BIENVENIDO ESTIMADO {nombre.upper()} LE DAMOS LA COORDIAL BIENVENIDA ESPERO QUE SE ENCUENTRE MUY BIEN EL DIA DE HOY ES UN GUSTO PODER SERVIRLE")
    elif opcion == 2:
        while True:
            print("****MENU DE PREGUNTAS")
            print("1. PREGUNTA 1")
            print("2. PREGUNTA 2")
            print("3. PREGUNTA 3")
            print("4. PREGUNTA 4")
            print("5. PREGUNTA 5")
            print("6. PREGUNTA 5")
            print("7. PREGUNTA 7")
            print("8. PREGUNTA 8")
            print("9. PREGUNTA 9")
            print("10. PREGUNTA 10")
            print("11. PREGUNTA 11")
            print("12. SALIR A MENU USUARIOS")
            respuestas = int(input("Ingrese una opcion: "))
            if respuestas == 1:
                print(f"LA RESPUESTA DE LA PREGUNTA 1 ES: ", pregunta1({1, 2, 3, 4}, {3, 4, 5}))
            elif respuestas == 2:
                print(f"LA RESPUESTA DE LA PREGUNTA 2 ES ", pregunta2())
            elif respuestas == 3:
                print(f"LA RESPUESTA DE LA PREGUNTA 3 ES ", pregunta3("Paute y"))
            elif respuestas == 4:
                print(f"LA RESPUESTA DE LA PREGUNTA 4 ES :", pregunta4())
            elif respuestas == 5:
                print(f"LA RESPUESTA DE LA PREGUNTA 5 ES :", pregunta5("aprendo Python en TEC"))
            elif respuestas == 6:
                print(f"LA RESPUESTA DE LA PREGUNTA 6 ES: " , end= " ")
                pregunta6(range(3,0,-1))
                print()
            elif respuestas == 7:
                print(f"LA RESPUESTA DE LA PREGUNTA 7 ES: ", end= " ")
                pregunta7([2, 4, 6])
            elif respuestas == 8:
                print(f"LA RESPUESTA DE LA PREGUNTA 8 ES: ", end= " ")
                pregunta8([1, 2, 3, 4])
                print()
            elif respuestas == 9:
                print(f"LA RESPUESTA DE LA PREGUNTA 9 ES: ", pregunta9([1, 2, 3, 4]))
            elif respuestas == 10:
                print(f"LA RESPUESTA DE LA PREGUNTA 10 ES: ", end= " ")
                pregunta10(range(1,10,3))
                print()
            elif respuestas == 11:
                print(f"LA RESPUESTA DE LA PREGUNTA 11 ES: ")
                pregunta11([8.5, 6.0, 9.75, 4.5, 7.0, 10.0, 5.25])
            elif respuestas == 12:
                print("SALIENDO.......")
                break;
            else:
                print("ESA OPCION NO EXISTE")
    elif opcion == 3:
        print(f"HASTA LA PROXIMA FUE UN GUSTO CONOCERTE")
        break;
    else:
        print("ESA OPCION NO EXISTE")

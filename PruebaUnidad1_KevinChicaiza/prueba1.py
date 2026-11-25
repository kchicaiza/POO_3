class Tanque:
    def __init__(self, codigo, combustible, precio, galones):
        self.codigo = codigo
        self.combustible = combustible
        self.precio = precio
        self.galones = galones

    def despachar(self, cantidad):
        if cantidad <= 0:
            print("Error: La cantidad solicitada debe ser mayor a cero")
            return False
        elif cantidad > self.galones:
            print (f"Error: solo hay {self.galones} galones")
            return False
        else:
            self.galones -= cantidad
            return True

    def __str__(self):
        return f"{self.codigo:<8}{self.combustible:<14}${self.precio:<11.2f}{self.galones:>8}"

lista_tanques = []
tanque1= Tanque(1, "Extra", 2.72, 500)
tanque2= Tanque(2, "Diesel", 1.80, 300)
lista_tanques.append(tanque1)
lista_tanques.append(tanque2)
opcion = 0
while opcion !=4:

    print (
        """
        ********************MENU*********************
        1. Registrar tanque   3. Despachar combustible
        2. Mostrar tanques   4. Salir 
        """
    )
    try:
        opcion = int(input("Ingrese un numero: "))
        if opcion==1:
            codigo = len(lista_tanques) + 1
            combustible  = input("Ingrese el combustible del tanque: ")
            precio = float(input("Ingrese el precio del combustible: "))
            galones = int(input("Ingrese los galones del combustible: "))
            tanque = Tanque(codigo, combustible, precio, galones)
            lista_tanques.append(tanque)
            print(f"Registrado con el codigo {codigo}")
        elif opcion==2:
            for i in lista_tanques:
                print(i)
        elif opcion==3:
            codigo = int(input("Ingrese el codigo del tanque: "))
            cantidad = int(input("Ingrese la cantidad de combustible: "))
            encontrado = False
            for i in lista_tanques:
                if codigo == i.codigo:
                    encontrado = True
                    resultado = i.despachar(cantidad)
                    if resultado == True:
                        print(f"Listo quedan {i.galones} galones")    
                    break
            if encontrado == False:
                print("Error: No existe ese codigo")
        elif opcion==4:
            print("Saliendo......")
        else:
            print("La opcion no existe en el menu")
    except ValueError:
        print("Dato incorrecto escriba un numero")
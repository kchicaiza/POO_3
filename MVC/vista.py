class VistaTanques:
    def menu(self):
        print (
            """
            ********************GASOLINERA EL ARENAL*********************
            1. Registrar tanque   3. Despachar combustible
            2. Mostrar tanques   4. Salir 
            """
        )
        opcion = int(input("Ingrese un numero: "))
        return opcion
    
    def pedir_datos(self):
        combustible  = input("Ingrese el combustible del tanque: ")
        precio = float(input("Ingrese el precio del combustible: "))
        galones = int(input("Ingrese los galones del combustible: "))
        return combustible, precio, galones
    
    def pedir_codigo(self):
        codigo = int(input("Ingrese el codigo del tanque: "))
        return codigo

    def pedir_cantidad(self):
        cantidad = int(input("Ingrese la cantidad de combustible: "))
        return cantidad

    def mensaje(self, mensaje):
        print(mensaje)

    def mostrar_tanques(self, tanques):
        for i in tanques:
            print(i)
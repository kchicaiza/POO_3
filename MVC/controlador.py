class ControladorTanques:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self): 
        opcion = ""
        while opcion !=4:
            opcion = self.vista.menu()
            if opcion==1:
                try:
                    combustible, precio, galones = self.vista.pedir_datos()
                    codigo = self.modelo.agregar(combustible, precio, galones)
                    self.vista.mensaje(f"Registrado con el codigo {codigo}")
                except ValueError:
                    self.vista.error("Datos ingresados incorrectamente")
            elif opcion==2:
                self.vista.mostrar_tanques(self.modelo.tanques)
            elif opcion==3:
                try:
                    tanque = self.modelo.buscar(self.vista.pedir_codigo())
                    if tanque != None:
                        cantidad = self.vista.pedir_cantidad()
                        estado, mensaje = tanque.despachar(cantidad)
                        if estado == True:
                            self.vista.mensaje(mensaje)
                        else:
                            self.vista.error(mensaje)
                    else:
                        self.vista.error("No existe ese codigo")
                except ValueError:
                    print("Dato incorrecto")
            elif opcion==4:
                self.vista.mensaje("Hasta la proxima")


    
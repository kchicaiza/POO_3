
def numero_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un numero entero")

opcion = 0
while opcion != 6:
    print( 
        """
        *****Sistemas de Calificaciones*****
        1. Registar estudiante
        2. Mostrar estudiantes
        3. Calcular promedio general
        4 Buscar estudiante
        5. Guardar informacion en archivo 
        6. Salir
        """
    )
    opcion = numero_entero("Ingrese un numero: ")
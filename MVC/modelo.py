class Tanque:
    def __init__(self, codigo, combustible, precio, galones):
        self.codigo = codigo
        self.combustible = combustible
        self.precio = precio
        self.galones = galones

    def despachar(self, cantidad):
        if cantidad <= 0:
            return False, "Error: La cantidad solicitada debe ser mayor a cero"
        elif cantidad > self.galones:
            return False, f"Error: solo hay {self.galones} galones"
        else:
            self.galones -= cantidad
            return True, f"Listo quedan {self.galones} galones"

    def __str__(self):
        return f"{self.codigo:<8}{self.combustible:<14}${self.precio:<11.2f}{self.galones:>8}"

class ListaTanques:
    def __init__(self):
        self.tanques=[]
        self.cargar()

    def cargar(self):
        lista=[
            Tanque(1, "Extra", 2.72, 500),
            Tanque(2, "Diesel", 1.80, 300)
        ]
        for i in lista:
            self.tanques.append(i)

    def agregar(self, combustible, precio, galones):
        codigo = len(self.tanques) + 1
        tanque = Tanque(codigo, combustible, precio, galones)
        self.tanques.append(tanque)
        return codigo


    def buscar(self, codigo):
        for i in self.tanques:
            if(i.codigo==codigo):
                return i

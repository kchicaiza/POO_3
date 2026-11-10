#Listas
notas = [10,8,9,5]
print(f"Lista de notas: {notas}")
print(f"Segunda nota: {notas[1]}")
notas.append(20)
notas.insert(1,10)
print(f"Longitud de la lista: {len(notas)}")
print(f"Última nota: {notas[-1]}")
print(f"Suma de las notas: {sum(notas)}")
print(f"Primera nota: {notas[0]}")
print(f"Las dos últimas notas: {notas[-2:]}")
print(f"Las dos primeras notas: {notas[:2]}")
print(f"Nota mínima: {min(notas)}")
notas.remove(9)
print(f"Lista de notas después de eliminar la nota 9: {notas}") 
sorted(notas)
print(f"Lista de notas ordenadas: {notas}") 

#Tupla
meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
print(meses[0])
print(meses[-1])
# meses[3] = "Mes 15" #Da error porque las tuplas son inmutables 

#Dicccionario
estudiante = {
    "cedula": "0106907009",
    "nombre": "Kevin Chicaiza",
    "correo": "kchicaizabravo@gmail.com",
    "celular": "0987949133",
    "notas" : [10, 9 , 8, 7, 6]
}

print(f"Nombre: {estudiante["nombre"]}")
print(f"Claves: {estudiante.keys()}")

#conjunto
conjunto_a = {1,1,5,4,6,8}
conjunto_b = {1,9,6,5,4}
print(f"Interseccion: {conjunto_a & conjunto_b}")
print(f"Union: {conjunto_a | conjunto_b}")

#Tarea
socio = {
    "cedula": "0102030405",                 
    "nombre": "  ana lucía pérez ",          
    "edad": 34,                              
    "activo": True,                          
    "garante": None,                         
    "cuentas": [                             
        {"numero": "AH-001", "tipo": "ahorros", "saldo": 1520.75},
        {"numero": "PF-010", "tipo": "plazo fijo", "saldo": 5000.0},
        {"numero": "AH-002", "tipo": "ahorros", "saldo": 80.5},
    ],
}

print(socio["nombre"].strip())
print(socio["nombre"].strip().title())
print(f"Cedula: {socio["cedula"]} | Edad: {socio['edad']}")
print(f"Activo: {socio['activo']}")
listas_cuentas = socio["cuentas"][2]["saldo"]
print(listas_cuentas)


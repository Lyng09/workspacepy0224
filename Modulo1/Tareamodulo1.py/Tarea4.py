#4.Realizar un programa que filtre si eres apto para registrar un negocio ,condiciones: 
# mayor de edad , tener ruc y tener un nombre comercial ,los inputs son si y /o no . 
# la salida debe ser si esta apto o no para abrir un comercio.

print("ingrese sus datos")
nombre=input("ingrese su nombre: ")
edad=int(input("ingrese su edad: "))
RUC=input("¿Tiene RUC? (si/no): ").lower() == "si"
nombre_comercial=input("¿Tiene nombre comercial? (si/no): ").lower() == "si"

if edad>=18 and RUC and nombre_comercial:
    print ("Estas apto para abrir un negocio")
else:
    print("No cumples con todas las condiciones para abrir un negocio")
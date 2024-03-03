#4.Realizar un programa que filtre si eres apto para registrar un negocio ,condiciones: 
# mayor de edad , tener ruc y tener un nombre comercial ,los inputs son si y /o no . 
# la salida debe ser si esta apto o no para abrir un comercio.

print("ingrese sus datos")
nombre=input("ingrese su nombre: ")
edad=int(input("ingrese su edad: "))
RUC=int(input("ingrese su RUC: "))
Nombre_comercial=("ingrese su nombre comercial: ")

if ((edad>=18) and (RUC)
    salario=float(salario)
    if salario<10000:
        tasa=0
    elif salario<18000:
        tasa=5
    elif salario<25000:
        tasa=10
    else:
        tasa=25

    
    impuesto=salario*(tasa/100)
    correo=input("ingrese su correo: ")
    msg=f"su impuesto sera {impuesto} le enviaremos a su correo, Gracias"
    print(msg)

else:
    msgError=f"hola {nombre}, usted no califica"
    print(msgError)
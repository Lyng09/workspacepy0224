### crear una calculadora de impuest0 o taxes en base al salario
# reglas => el sueldo se cobra solo a los mayores de edad
# regla2 tasa para sueldos menores de 10k anual es 0 
#menor a 18k es 5, menor a 25 k es 10 y luego todas las igtes es 15


print("ingrese sus datos")
nombre=input("ingrese su nombre: ")
edad=int(input("ingrese su edad: "))
salario=input("ingrese su salario: ")

if edad>=18:
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


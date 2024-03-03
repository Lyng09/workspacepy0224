#3.Realizar un programa que nos pida el ingreso total de un hogar y vaya pidiendo posibles gastos
#Como resultado debe decir  todos los egresos y el ahorro.

nombre=input("ingrese su nombre: ")
ingreso=float(input("ingrese sus ingresos totales: "))
msg="Ingrese sus datos"
print(msg)
alimentacion=float(input("Alimentos: "))
pasajes=float(input("Pasajes: "))
servicios_basicos=float(input("Servicios basicos: "))
alquiler=float(input("Alquiler: "))
otros_gastos=float(input("Otros gastos: "))

gastos=alimentacion+pasajes+servicios_basicos+alquiler+otros_gastos
Ahorro=ingreso-gastos
msg1=f"Sus egresos son {gastos} por lo tanto esta ahorrando {Ahorro}"
print(msg1)



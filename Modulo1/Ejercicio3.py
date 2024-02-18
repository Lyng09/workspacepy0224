#diversas formas de ver un print 
"""
nombre="datux"
msg0="Hola " + nombre
msg1="Hola {}" .format (nombre)
msg2= "Hola {nombre}"

print(msg0)
print(msg1)
print(msg2)
"""

nombre=input("ingrese su nombre:")
edad=input("ingrese su edad:")
correo=input("ingrese su correo:")

msg0="hola "+nombre + "" + edad +" "+correo
msg1=f"Hola {nombre} {edad} {correo}"
print(msg0, "\n" , msg1)



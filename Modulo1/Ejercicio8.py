import sys
sys.argv
dataYear = sys.argv[1]
dataCurrent=input("ingrese el año actual")

if dataYear <=2012 and (type(dataCurrent)==int):
    print ("los datos para mostrar el reporte ...")

else:
    print("los años son incorrectos")
    
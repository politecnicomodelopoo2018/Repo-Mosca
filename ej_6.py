from class_vehiculo import Auto, Camioneta
from class_empresa import Empresa

emp_ford = Empresa("Ford")

autos = []
autos.append(Auto("RGB 256", 4, 2011, False))
autos.append(Auto("GAY 696", 4, 2007, True))
autos.append(Auto("AHT 127", 4, 2014, True))
for a in autos: emp_ford.lista_autos.append(a)

camionetas = []
camionetas.append(Camioneta("RHY 274", 4, 1999, 60))
camionetas.append(Camioneta("TRY 745", 4, 2000, 45))
camionetas.append(Camioneta("ZZY 991", 4, 2026, 250))
for c in camionetas: emp_ford.lista_camionetas.append(c)

print("Autos:")
for i, a in enumerate(emp_ford.lista_autos):
    print("#" + str(i+1) + ":")
    print("    Patente: " + a.patente)
    print("    Ruedas: " + str(a.cant_ruedas))
    print("    Año de fabricacion: " + str(a.año_fab))
    print("    Descapotable: " + ("Si" if a.descapotable else "No"))

print("\nCamionetas:")
for i, c in enumerate(emp_ford.lista_camionetas):
    print("#" + str(i+1) + ":")
    print("    Patente: " + c.patente)
    print("    Ruedas: " + str(c.cant_ruedas))
    print("    Año de fabricacion: " + str(c.año_fab))
    print("    Carga: " + str(c.carga) + " kg")

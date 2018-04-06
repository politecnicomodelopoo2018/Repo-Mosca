from class_plato import Plato
from class_familia import Familia
from class_persona import Persona

plato_ravioles = Plato("Ravioles", 200)
plato_cereales = Plato("Cereales", 150)
plato_spaghetti = Plato("Spaghetti", 230)
plato_hamburguesa = Plato("Hamburguesa", 350)
plato_hamburguesa_mac = Plato("Hamburguesa del Mac", 3500)

fam = Familia("Gonzalez")

pedro = Persona("Pedro", "16/02/1989")
fam.agregarPersona(pedro)

maria = Persona("Maria", "21/06/1991")
fam.agregarPersona(maria)

enrique = Persona("Enrique", "12/11/2012")
fam.agregarPersona(enrique)

pedro.consumirPlato(plato_ravioles)
pedro.consumirPlato(plato_cereales)
pedro.consumirPlato(plato_hamburguesa)

maria.consumirPlato(plato_spaghetti)
maria.consumirPlato(plato_ravioles)

enrique.consumirPlato(plato_hamburguesa)
enrique.consumirPlato(plato_hamburguesa_mac)
enrique.consumirPlato(plato_spaghetti)

print("Calorias consumidas por Pedro Gonzalez: " + str(pedro.calorias_consumidas))
print("Calorias consumidas por Maria Gonzalez: " + str(maria.calorias_consumidas))
print("Calorias consumidas por Enrique Gonzalez: " + str(enrique.calorias_consumidas))

print("\n")
print("Promedio calorias consumidas en la familia Gonzalez: " + str(fam.promCalorias()))
print("Mayor consumidor de calorias: " + fam.pers_mayorCalorias().nombre)
print("Menor consumidor de calorias: " + fam.pers_menorCalorias().nombre)
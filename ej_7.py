from class_sistema import Sistema
from ej_7_loops import loop_alumno, loop_profesor, loop_plato#, loop_pedido

sist = Sistema()

fin = False
while not fin:
    print("\n-------- BUFET --------")
    print("1 - Crear/Modificar Alumno")
    print("2 - Crear/Modificar Profesor")
    print("3 - Crear/Modificar Plato")
    print("4 - Crear/Modificar Pedido")
    print("5 - Salir")
    print("Escriba el numero correspondiente para continuar:")

    inp = input()
    if inp == "1":
        loop_alumno(sist)
    elif inp == "2":
        loop_profesor(sist)
    elif inp == "3":
        loop_plato(sist)
    #elif inp == "4":
    #    loop_pedido(sist)
    elif inp == "5":
        print("Finalizando...")
        fin = True
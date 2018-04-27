from class_sistema import Sistema
from ej_7_loops import loop_alumno, loop_profesor, loop_plato, loop_pedido

def ej_pause():
    input("\nPresione Enter para continuar...\n")

sist = Sistema()

fin = False
while not fin:
    print("\n-------- BUFET --------")
    print("1 - Crear/Modificar Alumno")
    print("2 - Crear/Modificar Profesor")
    print("3 - Crear/Modificar Plato")
    print("4 - Crear/Modificar Pedido")
    print("5 - Listar platos a cocinar en un dia")
    print("6 - Salir")
    print("Escriba el numero correspondiente para continuar:")

    inp = input()
    if inp == "1":
        loop_alumno(sist)
    elif inp == "2":
        loop_profesor(sist)
    elif inp == "3":
        loop_plato(sist)
    elif inp == "4":
        if len(sist.lista_platos) == 0:
            print("\nNo hay platos con los cuales realizar pedidos!")
            ej_pause()
        elif len(sist.lista_alumnos) == 0 and len(sist.lista_profesores) == 0:
            print("\nNo hay alumnos ni profesores con los cuales realizar pedidos!")
            ej_pause()
        else:
            loop_pedido(sist)
    elif inp == "5":
        print("Ingrese el dia:")
        tmp_platos = sist.platosDia(int(input()))
        if len(tmp_platos) > 0:
            for p in tmp_platos:
                print(p.info_string())
        else:
            print("No hay platos en ese dia!")

        ej_pause()

    elif inp == "6":
        print("Finalizando...")
        fin = True
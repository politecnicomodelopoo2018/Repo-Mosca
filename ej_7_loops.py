from copy import deepcopy
from class_persona import Profesor

def loop_alumno(sist):
    fin_loop = False
    while not fin_loop:
        print("\n-------- CREAR/MODIFICAR ALUMNO --------")
        print("# Alumnos existentes: " + str(len(sist.lista_alumnos)))
        print("1 - Crear nuevo alumno")
        print("2 - Modificar alumno existente")
        print("3 - Eliminar alumno")
        print("4 - Volver")

        fin_subloop = False
        tmp_inp = input()
        if tmp_inp == "1":  # Crear nuevo alumno
            new_alumno = sist.crearAlumno("", "", "")

            print("Ingrese el nombre:")
            new_alumno.nombre = input()
            print("Ingrese el apellido:")
            new_alumno.apellido = input()
            print("Ingrese la division:")
            new_alumno.division = input()

        elif tmp_inp == "2":  # Modificar alumno existente
            while not fin_subloop:
                if len(sist.lista_alumnos) > 0:
                    print("Modificar alumno...")
                    for i, alum in enumerate(sist.lista_alumnos):
                        print(str(i + 1) + " - " + alum.info_string())
                    print(str(len(sist.lista_alumnos) + 1) + " - Volver")

                    tmp_inp = int(input()) - 1
                    if tmp_inp >= 0 and tmp_inp < len(sist.lista_alumnos):
                        tmp_alum = sist.lista_alumnos[tmp_inp]
                        print("Modificando alumno " + tmp_alum.info_string())

                        print("Ingrese el nuevo nombre:")
                        tmp_alum.nombre = input()

                        print("Ingrese el nuevo apellido:")
                        tmp_alum.apellido= input()

                        print("Ingrese la nueva division:")
                        tmp_alum.division = input()

                    elif tmp_inp == len(sist.lista_alumnos):
                        fin_subloop = True

                else:
                    print("No hay mas alumnos que modificar!")

        elif tmp_inp == "3": # Eliminar alumno existente
            while not fin_subloop:
                if len(sist.lista_alumnos) > 0:
                    print("Eliminar alumno...")
                    for i, alum in enumerate(sist.lista_alumnos):
                        print(str(i + 1) + " - " + alum.info_string())
                    print(str(len(sist.lista_alumnos) + 1) + " - Volver")

                    tmp_inp = int(input()) - 1
                    if tmp_inp >= 0 and tmp_inp < len(sist.lista_alumnos):
                        sist.lista_alumnos.remove(sist.lista_alumnos[tmp_inp])

                    elif tmp_inp == len(sist.lista_alumnos):
                        fin_subloop = True

                else:
                    print("No hay mas alumnos que eliminar!")

        elif tmp_inp == "4":
            fin_loop = True


def loop_profesor(sist):
    fin_loop = False
    while not fin_loop:
        print("\n-------- CREAR/MODIFICAR PROFESOR --------")
        print("# Profesores existentes: " + str(len(sist.lista_profesores)))
        print("1 - Crear nuevo profesor")
        print("2 - Modificar profesor existente")
        print("3 - Eliminar profesor")
        print("4 - Volver")

        fin_subloop = False
        tmp_inp = input()
        if tmp_inp == "1":  # Crear nuevo profesor
            new_prof = sist.crearProfesor("", "", 0)

            print("Ingrese el nombre:")
            new_prof.nombre = input()
            print("Ingrese el apellido:")
            new_prof.apellido = input()
            print("Ingrese el porcentaje de descuento:")
            new_prof.descuento = int(input())

        elif tmp_inp == "2":  # Modificar profesor existente
            while not fin_subloop:
                if len(sist.lista_profesores) > 0:
                    print("Modificar profesor...")
                    for i, prof in enumerate(sist.lista_profesores):
                        print(str(i + 1) + " - " + prof.info_string())
                    print(str(len(sist.lista_profesores) + 1) + " - Volver")

                    tmp_inp = int(input()) - 1
                    if tmp_inp >= 0 and tmp_inp < len(sist.lista_profesores):
                        tmp_prof = sist.lista_profesores[tmp_inp]
                        print("Modificando profesor " + tmp_prof.info_string())

                        print("Ingrese el nuevo nombre:")
                        tmp_prof.nombre = input()

                        print("Ingrese el nuevo apellido:")
                        tmp_prof.apellido = input()

                        print("Ingrese el nuevo porcentaje de descuento:")
                        tmp_prof.descuento = int(input())

                    elif tmp_inp == len(sist.lista_profesores):
                        fin_subloop = True

                else:
                    print("No hay mas profesores que modificar!")

        elif tmp_inp == "3":  # Eliminar profesor existente
            while not fin_subloop:
                if len(sist.lista_profesores) > 0:
                    print("Eliminar profesor...")
                    for i, prof in enumerate(sist.lista_profesores):
                        print(str(i + 1) + " - " + prof.info_string())
                    print(str(len(sist.lista_profesores) + 1) + " - Volver")

                    tmp_inp = int(input()) - 1
                    if tmp_inp >= 0 and tmp_inp < len(sist.lista_profesores):
                        sist.lista_profesores.remove(sist.lista_profesores[tmp_inp])

                    elif tmp_inp == len(sist.lista_profesores):
                        fin_subloop = True

                else:
                    print("No hay mas profesores que eliminar!")
                    fin_subloop = True

        elif tmp_inp == "4":
            fin_loop = True

def loop_plato(sist):
    fin_loop = False
    while not fin_loop:
        print("\n-------- CREAR/MODIFICAR PLATO --------")
        print("# Platos existentes: " + str(len(sist.lista_platos)))
        print("1 - Crear nuevo plato")
        print("2 - Modificar plato existente")
        print("3 - Eliminar plato")
        print("4 - Volver")

        fin_subloop = False
        tmp_inp = input()
        if tmp_inp == "1":  # Crear nuevo plato
            new_plato = sist.crearPlato("", 0)

            print("Ingrese el nombre:")
            new_plato.nombre = input()
            print("Ingrese el precio:")
            new_plato.precio = int(input())

        elif tmp_inp == "2":  # Modificar plato existente
            while not fin_subloop:
                if len(sist.lista_platos) > 0:
                    print("Modificar plato...")
                    for i, plato in enumerate(sist.lista_platos):
                        print(str(i + 1) + " - " + plato.info_string())
                    print(str(len(sist.lista_platos) + 1) + " - Volver")

                    tmp_inp = int(input()) - 1
                    if tmp_inp >= 0 and tmp_inp < len(sist.lista_platos):
                        tmp_plato = sist.lista_platos[tmp_inp]
                        print("Modificando plato " + tmp_plato.info_string())

                        print("Ingrese el nuevo nombre:")
                        tmp_plato.nombre = input()

                        print("Ingrese el nuevo precio:")
                        tmp_plato.precio = int(input())

                    elif tmp_inp == len(sist.lista_platos):
                        fin_subloop = True

                else:
                    print("No hay mas platos que modificar!")
                    fin_subloop = True

        elif tmp_inp == "3":  # Eliminar plato existente
            while not fin_subloop:
                if len(sist.lista_platos) > 0:
                    print("Eliminar plato...")
                    for i, plato in enumerate(sist.lista_platos):
                        print(str(i + 1) + " - " + plato.info_string())
                    print(str(len(sist.lista_platos) + 1) + " - Volver")

                    tmp_inp = int(input()) - 1
                    if tmp_inp >= 0 and tmp_inp < len(sist.lista_platos):
                        sist.lista_platos.remove(sist.lista_platos[tmp_inp])

                    elif tmp_inp == len(sist.lista_platos):
                        fin_subloop = True

                else:
                    print("No hay mas platos que eliminar!")
                    fin_subloop = True

        elif tmp_inp == "4":
            fin_loop = True

def loop_pedido(sist):
    fin_loop = False
    while not fin_loop:
        print("\n-------- CREAR/MODIFICAR PEDIDO --------")
        print("# Pedidos existentes: " + str(len(sist.lista_pedidos)))
        print("1 - Crear nuevo pedido")
        print("2 - Modificar pedido existente")
        print("3 - Eliminar pedido")
        print("4 - Volver")

        fin_subloop = False
        tmp_inp = input()
        if tmp_inp == "1":  # Crear nuevo pedido
            new_pedido = sist.crearPedido([], None, None, 0)

            # Fecha del pedido
            print("Ingrese el dia del pedido:")
            new_pedido.fecha_creacion = int(input())

            # Plato del pedido
            print("\n")
            for i, pl in enumerate(sist.lista_platos):
                print(str(i) + " - " + pl.info_string())
            print("Ingrese el numero del plato para el pedido:")

            tmp_subloop = False
            while not tmp_subloop:
                tmp_inp = int(input())
                if not (tmp_inp >= 0 and tmp_inp < len(sist.lista_platos)):
                    print("Entrada incorrecta!\n")
                else:
                    tmp_subloop = True

            new_pedido.plato = deepcopy(sist.lista_platos[tmp_inp])

            # Cliente del pedido
            print("\n")
            tmp_clientes = sist.lista_alumnos + sist.lista_profesores
            for i, cl in enumerate(tmp_clientes):
                print(str(i) + " - " + cl.info_string())
            print("Ingrese el numero del cliente para el pedido:")

            tmp_subloop = False
            while not tmp_subloop:
                tmp_inp = int(input())
                if not (tmp_inp >= 0 and tmp_inp < len(tmp_clientes)):
                    print("Entrada incorrecta!\n")
                else:
                    tmp_subloop = True

            new_pedido.cliente = tmp_clientes[tmp_inp]

            # Aplicar descuento al plato
            if type(new_pedido.cliente) is Profesor:
                new_pedido.plato.precio *= (100 - new_pedido.cliente.descuento) / 100

            print("Ingrese la hora de entrega del pedido, con el formato <Hora>:<Minutos> (por ej. 20:30):")
            new_pedido.hora_entrega = [int(h) for h in input().split(":")]

        elif tmp_inp == "2":  # Modificar pedido existente
            while not fin_subloop:
                if len(sist.lista_pedidos) > 0:
                    print("Modificar pedido...")
                    for i, pedido in enumerate(sist.lista_pedidos):
                        print(str(i + 1) + " - " + pedido.info_string())
                    print(str(len(sist.lista_pedidos) + 1) + " - Volver")

                    tmp_inp = int(input()) - 1
                    if tmp_inp >= 0 and tmp_inp < len(sist.lista_pedidos):
                        tmp_pedido = sist.lista_pedidos[tmp_inp]
                        print("Modificando pedido [" + tmp_pedido.info_string() + "]")

                        # Fecha del pedido
                        print("Ingrese el nuevo dia del pedido:")
                        tmp_pedido.fecha_creacion = int(input())

                        # Plato del pedido
                        for i, pl in enumerate(sist.lista_platos):
                            print(str(i) + " - " + pl.info_string())
                        print("Ingrese el nuevo numero del plato para el pedido:")

                        tmp_subloop = False
                        while not tmp_subloop:
                            tmp_inp = int(input())
                            if not (tmp_inp >= 0 and tmp_inp < len(sist.lista_platos)):
                                print("Entrada incorrecta!\n")
                            else:
                                tmp_subloop = True

                        tmp_pedido.plato = deepcopy(sist.lista_platos[tmp_inp])

                        # Cliente del pedido
                        print("\n")
                        tmp_clientes = sist.lista_alumnos + sist.lista_profesores
                        for i, cl in enumerate(tmp_clientes):
                            print(str(i) + " - " + cl.info_string())
                        print("Ingrese el numero del cliente para el pedido:")

                        tmp_subloop = False
                        while not tmp_subloop:
                            tmp_inp = int(input())
                            if not (tmp_inp >= 0 and tmp_inp < len(tmp_clientes)):
                                print("Entrada incorrecta!\n")
                            else:
                                tmp_subloop = True

                        tmp_pedido.cliente = tmp_clientes[tmp_inp]

                        # Aplicar descuento al plato
                        if type(new_pedido.cliente) is Profesor:
                            new_pedido.plato.precio *= (100 - new_pedido.cliente.descuento) / 100

                        print("Ingrese la hora de entrega del pedido, con el formato <Hora>:<Minutos> (por ej. 20:30):")
                        tmp_pedido.hora_entrega = [int(h) for h in input().split(":")]

                    elif tmp_inp == len(sist.lista_pedidos):
                        fin_subloop = True

                else:
                    print("No hay mas pedidos que modificar!")
                    fin_subloop = True

        elif tmp_inp == "3":  # Eliminar pedido existente
            while not fin_subloop:
                if len(sist.lista_pedidos) > 0:
                    print("Eliminar pedido...")
                    for i, pedido in enumerate(sist.lista_pedidos):
                        print(str(i + 1) + " - " + pedido.info_string())
                    print(str(len(sist.lista_pedidos) + 1) + " - Volver")

                    tmp_inp = int(input()) - 1
                    if tmp_inp >= 0 and tmp_inp < len(sist.lista_pedidos):
                        sist.lista_pedidos.remove(sist.lista_pedidos[tmp_inp])

                    elif tmp_inp == len(sist.lista_pedidos):
                        fin_subloop = True

                else:
                    print("No hay mas pedidos que eliminar!")
                    fin_subloop = True

        elif tmp_inp == "4":
            fin_loop = True
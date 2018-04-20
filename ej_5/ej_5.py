# -*- coding: utf-8 -*-

from ej_5.class_sistema import Sistema

sist = Sistema()

# Artistas
art_guido = sist.crearArtista("Guido", "Weiser", [1994, 6, 15])
art_pablo = sist.crearArtista("Pablo", "Gonzalez", [1991, 4, 8])
art_ale = sist.crearArtista("Alejandro", "Mosca", [2000, 7, 12])

# Autores
aut_hernan = sist.crearAutor("Hernan", "Gonzalez", [1994, 6, 15], "Mexico")
aut_jorge = sist.crearAutor("Jorge", "Heisenberg", [1983, 2, 21], "España")
aut_gerardo = sist.crearAutor("Gerardo", "Diaz", [1994, 11, 29], "Argentina")

# Albumes
alb_red = sist.crearAlbum("Red")
alb_green = sist.crearAlbum("Green")

# Canciones - Album Red
can_red_1 = sist.crearCancion("cancion red 1", [art_ale], [aut_jorge])
alb_red.lista_canciones.append(can_red_1)

can_red_2 = sist.crearCancion("cancion red 2", [art_ale, art_guido], [aut_hernan])
alb_red.lista_canciones.append(can_red_2)

can_red_3 = sist.crearCancion("cancion red 3", [art_guido], [aut_hernan, aut_jorge])
alb_red.lista_canciones.append(can_red_3)

# Canciones - Album Green
can_green_1 = sist.crearCancion("cancion green 1", [art_pablo, art_ale], [aut_jorge])
alb_green.lista_canciones.append(can_green_1)

can_green_2 = sist.crearCancion("cancion green 2", [art_pablo], [aut_jorge, aut_gerardo])
alb_green.lista_canciones.append(can_green_2)

can_green_3 = sist.crearCancion("cancion green 3", [art_pablo, art_ale, art_guido], [aut_gerardo])
alb_green.lista_canciones.append(can_green_3)

print("Albumes:")
for alb in sist.lista_albumes:
    print(alb.titulo)
    print("Artistas: ", end="")
    for art in alb.artistasParticipantes():
        print(art.nombre + " " + art.apellido + ", ", end='')

    print("") # Separar
    print("Mas influyente: " + alb.artistaInfluyente().nombre)
    print("\n")

print("Canciones por nacionalidad:")
tmp_naciones = ["Mexico", "España", "Argentina"]
for n in tmp_naciones:
    print(n + ": ", end='')
    for c in sist.cancionesNacionalidad(n):
        print(c.titulo + ", ", end='')
    print("")
from class_persona import Persona, Artista, Autor
from class_album_cancion import Album, Cancion

class Sistema(object):
        def __init__(self):
            self.lista_canciones = []
            self.lista_albumes = []

            self.lista_artistas = []
            self.lista_autores = []

        # Creacion de objetos
        def crearCancion(self, titulo):
            tmp_cancion = Cancion(titulo)
            self.lista_canciones.append(tmp_cancion)
            return tmp_cancion

        def crearAlbum(self, titulo):
            tmp_album = Album(titulo)
            self.lista_albumes.append(tmp_album)
            return tmp_album

        def crearArtista(self, nombre, apellido, fechanac):
            tmp_artista = Artista(nombre, apellido, fechanac)
            self.lista_artistas.append(tmp_artista)
            return tmp_artista

        def crearAutor(self, nombre, apellido, fechanac, nacion):
            tmp_autor = Autor(nombre, apellido, fechanac, nacion)
            self.lista_autores.append(tmp_autor)
            return tmp_autor

        # Metodos
        def cancionesNacionalidad(self, nacion):
            tmp_canciones = []
            for autor in self.lista_autores:
                if autor.nacionalidad == nacion:
                    for cancion in self.lista_canciones:

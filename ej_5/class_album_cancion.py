class Album(object):
    def __init__(self, titulo):
        self.titulo = titulo

        self.lista_canciones = []

    def artistasParticipantes(self):
        tmp_artistas = []
        for cancion in self.lista_canciones:
            for art in cancion.lista_artistas:
                if not art in tmp_artistas:
                    tmp_artistas.append(art)

        return tmp_artistas

    def artistaInfluyente(self):
        tmp_artistainf = None
        tmp_max = 0
        for art in self.artistasParticipantes():
            tmp_inf = 0
            for cancion in self.lista_canciones:
                if art in cancion.lista_artistas:
                    tmp_inf += 1

            if tmp_inf > tmp_max:
                tmp_artistainf = art
                tmp_max = tmp_inf

        return tmp_artistainf

class Cancion(object):
    def __init__(self, titulo, artistas = [], autores = []):
        self.titulo = titulo

        self.lista_artistas = artistas
        self.lista_autores = autores
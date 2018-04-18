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
        tmp_artistas = self.artistasParticipantes()
        for art in tmp_artistas:
            art = [art, 0]
            for cancion in self.lista_canciones:
                if art in cancion.lista_artistas:
                    art[1] += 1

        tmp_artistainf = None
        tmp_max = 0
        for art in tmp_artistas:
            if art[1] > tmp_max:
                tmp_artistainf = art[0]
                tmp_max = art[1]

        return tmp_artistainf

class Cancion(object):
    def __init__(self, titulo):
        self.titulo = titulo

        self.lista_artistas = []
        self.lista_autores = []
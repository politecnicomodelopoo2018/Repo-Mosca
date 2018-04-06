class Familia(object):
    def __init__(self, nombre):
        self.nombre = nombre

        self.lista_personas = []

    def agregarPersona(self, pers):
        self.lista_personas.append(pers)

    def promCalorias(self):
        cals = 0
        for pers in self.lista_personas:
            cals += pers.calorias_consumidas

        return cals / len(self.lista_personas)

    def pers_mayorCalorias(self):
        if len(self.lista_personas) == 0:
            return None

        tmp_pers = self.lista_personas[0]
        for pers in self.lista_personas:
            if pers.calorias_consumidas > tmp_pers.calorias_consumidas:
                tmp_pers = pers

        return tmp_pers

    def pers_menorCalorias(self):
        if len(self.lista_personas) == 0:
            return None

        tmp_pers = self.lista_personas[0]
        for pers in self.lista_personas:
            if pers.calorias_consumidas < tmp_pers.calorias_consumidas:
                tmp_pers = pers

        return tmp_pers
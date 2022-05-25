class Deportista():
    def __init__(self, añosPracticando, deporte = "Futbol"):
        self._deporte = deporte
        self._añosPracticando = añosPracticando

    def setDeporte(self, deporte):
        self._deporte = deporte
    def getDeporte(self):
        return self._deporte

    def setAñosPracticando(self, años):
        self._añosPracticando = años
    def getAñosPracticando(self):
        return self._añosPracticando 

        
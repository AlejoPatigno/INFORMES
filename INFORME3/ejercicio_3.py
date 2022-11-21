
class Automoviles:
    
    def __init__(self, color: str, personasSentadas: int, uso: str):
        self.color = color
        self.personasSentadas = personasSentadas
        self.uso = uso
    
    
    def acelerar(self, aceleracion: float, tiempo: float):
        v = aceleracion * tiempo
        return v

    def frenar(self, velocidad, desaceleracion):
        a = desaceleracion
        t= velocidad/a
        return t



FERRARI_458 = Automoviles("rojo", 2, "Deportivo")
MCLAREN_720S = Automoviles("negro", 4, "Deportivo")
AUTOLEGAL = Automoviles("blanco", 20, "Publico")


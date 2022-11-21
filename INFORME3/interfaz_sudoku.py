"""
     este modulo es la interfaz, donde tendremos la creacion del tablero, 
     explicacion de como se juega 

"""
import random

print(random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))

def explicarJuego():
    print("""
    
           este es el juego de sudoku.

           es un juego de solo un jugador, en forma de puzzle en el que tendremos 4 zonas 
           lo que tienes que hacer es completar el puzzle y asegurarte de que el mismo numero 
           no aparece dos veces en la misma linea, columna o  zona de las 4 posibles

           las disposiciones del juego son las siguientes:

               (0)  | (1)  | (2)  | (3)
               (4)  | (5)  | (6)  | (7)
               -------------------------
               (8)  | (9) | (10) | (11)
               (12) | (13) | (14) | (15)

           debe tener en cuenta que esta dividido en los cuadrantes (1,2,5,6),
           (3,4,7,8), (9,10,13,14) y (11,12,15,16). en donde iran los numeros 
           1, 2, 3, 4. el objetivo será llenar el tablero según las reglas antes dichas.  """) 

def dibujarTablero(tableroLogico:list):
    tableroVisual = """
                {}  | {} | {} | {}
                -------------------
                {}  | {} | {} | {}
                -------------------
                {}  | {} | {} | {}
                -------------------
                {}  | {} | {} | {}

    """.format(tableroLogico[0], tableroLogico[1],
               tableroLogico[2], tableroLogico[3],
               tableroLogico[4], tableroLogico[5],
               tableroLogico[6], tableroLogico[7],
               tableroLogico[8], tableroLogico[9],
               tableroLogico[10], tableroLogico[11],
               tableroLogico[12], tableroLogico[13],
               tableroLogico[14], tableroLogico[15],
               )
    tableroVisual = tableroVisual.replace("None", " ")
    print(tableroVisual)

def crearPistas(tableroLogico:list):
    
    import logica_sudoku as logica 
    import random
    c=0
    for i in range(0,5):
        posicion =int( random.choice([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
        caracter = random.choice([1,2,3,4])
        if logica.determinarError(tableroLogico,posicion, caracter):
            tableroLogico = logica.actualizarTableroLogico(tableroLogico, posicion, caracter)
            c=c+1
    dibujarTablero(tableroLogico)
    return tableroLogico

if __name__ == "__main__":
    explicarJuego()
    tablero1 = [None]*16
    tablero2 = ["x"]*16
    crearPistas(tablero1)
    dibujarTablero(tablero1)
    dibujarTablero(tablero2)
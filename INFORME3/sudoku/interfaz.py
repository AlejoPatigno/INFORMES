"""
     este modulo es la interfaz, donde tendremos la creacion del tablero, 
     explicacion de como se juega 

"""
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



if __name__ == "__main__":
    explicarJuego()
    tablero1 = [None]*16
    tablero2 = ["x"]*16
    dibujarTablero(tablero1)
    dibujarTablero(tablero2)
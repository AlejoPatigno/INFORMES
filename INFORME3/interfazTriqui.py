"""este modulo es la interfaz y con este modulo intentaremos crear la parte visual del juego triky
aqui deberá haber una pantalla de juego, decir quien tiene el turno y quien es el ganador """

def explicarJuego():
    explicacion=""" 
    Este es el juego 3 en linea

    Es un juego de 2 jugadores, para ganar debe completar 3 caracteres iguales en linea ("X"o "O")

    Para ingresar la posición en el juego, guiese con los siguientes numeros

    (0) | (1) | (2)
    ____|_____|_______
    (3) | (4) | (5)
    ____|_____|_______
    (6) | (7) | (8)
    
    """
    print(explicacion)
    input("...ingrese enter para empezar el juego....")
  
   
tableroLista = ["x", "o", None, None,None,None,None,None,None]

def dibujarTablero(tableroLogico:list):
    tableroVisual = """
                {}  | {} |  {}
                ------------- 
                {}  | {} |  {}
                ------------- 
                {}  | {} |  {}
    
    """.format(tableroLogico[0], tableroLogico[1],
               tableroLogico[2], tableroLogico[3],
               tableroLogico[4], tableroLogico[5],
               tableroLogico[6], tableroLogico[7],
               tableroLogico[8])

    print(tableroVisual)
    return tableroLogico

if __name__ == "__main__":
    explicarJuego()
    tablero1 = ["None"]*9
    tablero2= ["X"]*9
    
    dibujarTablero(tablero1)
    dibujarTablero(tablero2)

def imprimirTurno(caracter: str):

    if caracter == "None":
        print("es turno de X")
    elif caracter == "X":
        print("es turno de O")
    elif caracter == "O":
        print("es turno de X")
    else:
        print("Este caracter no está permitido")
    
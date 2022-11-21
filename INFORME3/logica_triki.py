"""este modulo es la logica y con este modulo haremos la parte logica del juego 
de 3 en linea. tendremos funciones de obtener tablero logico, actualizar el tablero logico, 
determinar ganador, determinar si la posicion de una jugada esta ocupada y tener una lista del 
tablero faltante """

def obtenerTableroLogico():

    tableroLogico=[None,None,None,None,None,None,None,None,None]

    return tableroLogico

def actualizarTableroLogico(tableroLogico, posicion, caracter):

    tableroLogico[posicion]=caracter

    return tableroLogico

def determinarGanador(tableroLogico):

    posicionesParaGanar=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    ganador=None
    for p1, p2, p3 in posicionesParaGanar:
        if (tableroLogico[p1] == tableroLogico[p2] == tableroLogico[p3]):
            if tableroLogico[p1] != None:
                ganador= tableroLogico[p1]
    
    return ganador

def determinarPosicionOcupada(tableroLogico, posicion):
    if tableroLogico[posicion] == None:
        validez=True
    else:
        validez=False
    return validez

def tableroFaltante(tableroLogico):
    tableroAzucar=[]
    for i in range(0,9):
        if tableroLogico[i] == None:
            tableroAzucar.append(i)
    return tableroAzucar

if __name__== "__main__":
    tablero = obtenerTableroLogico()
    tableroNuevo = actualizarTableroLogico(tablero, 0, "x")
    print(tableroNuevo)
    ganador =  determinarGanador(["x", "x", "x", None, None,None,None,None,None, ])
    print(ganador)


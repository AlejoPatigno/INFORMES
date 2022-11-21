"""
Este modulo contiene las funciones logicas
del juego:
* obtenerTableroLogico() => Retorna tablero logico de Nones
                            lista
* actualizarTableroLogico(tableroLogico, posicion, caracter) => retorna tablero logico actualizado
                                                                lista
* determinarSiGano(tableroLogico) => Retorna si usted a ganado el juego 
* tableroFaltante(tableroLogico) => Retorna una lista de posiciones faltantes en el juego                            
"""

def obtenerTableroLogico():
    tableroLogico = [None, None, None, None, None, None, None, None, None,
                     None, None, None, None, None, None, None]
    return tableroLogico

def actualizarTableroLogico(tableroLogico, posicion: int, caracter: int):
    if 0< caracter <=4:
        tableroLogico[posicion] = caracter
    else: print("numero invalido ")
    return tableroLogico

def determinarSiGano(tableroLogico):
    if None not in tableroLogico: return True
    else: return False
    

def tableroFaltante(tableroLogico):
    tableroSabroso=[]
    for i in range(0,16):
        if tableroLogico[i] == None:
            tableroSabroso.append(i)
    return tableroSabroso

def determinarError(tableroLogico,posicion, caracter: int):
    if caracter in (1,2,3,4):
        fila1 = [0,1,2,3]
        fila2 = [4,5,6,7]
        fila3 = [8,9,10,11]
        fila4 = [12,13,14,15]
        columna1 = [0,4,8,12]
        columna2 = [1,5,9,13]
        columna3 = [2,6,10,14]
        columna4 = [3,7,11,15]
        zona1 = [0,1,4,5]
        zona2 = [2,3,6,7]
        zona3 = [8,9,12,13]
        zona4 = [10,11,14,15]
        validez= True

        if posicion in fila1:
            lista1= fila1.copy()
            lista1.remove(posicion)
            for i in lista1:
                if caracter == tableroLogico[i]:
                    validez=False
        if posicion in fila2:
            lista2= fila2.copy()
            lista2.remove(posicion)
            for i in lista2:
                if caracter == tableroLogico[i]:
                    validez=False
        if posicion in fila3:
            lista3= fila3.copy()
            lista3.remove(posicion)
            for i in lista3:
                if caracter == tableroLogico[i]:
                    validez=False
        if posicion in fila4:
            lista4= fila4.copy()
            lista4.remove(posicion)
            for i in lista4:
                if caracter == tableroLogico[i]:
                    validez=False
        if posicion in columna1:
            lista5= columna1.copy()
            lista5.remove(posicion)
            for i in lista5:
                if caracter == tableroLogico[i]:
                    validez=False
        if posicion in columna2:
            lista6= columna2.copy()
            lista6.remove(posicion)
            for i in lista6:
                if caracter == tableroLogico[i]:
                    validez=False
        if posicion in columna3:
            lista7= columna3.copy()
            lista7.remove(posicion)
            for i in lista7:
                if caracter == tableroLogico[i]:
                    validez=False
        if posicion in columna4:
            lista8= columna4.copy()
            lista8.remove(posicion)
            for i in lista8:
                if caracter == tableroLogico[i]:
                    validez=False
        if posicion in zona1:
            lista9= zona1.copy()
            lista9.remove(posicion)
            for i in lista9:
                if caracter == tableroLogico[i]:
                    validez=False
        if posicion in zona2:
            lista10= zona2.copy()
            lista10.remove(posicion)
            for i in lista10:
                if caracter == tableroLogico[i]:
                    validez=False
        if posicion in zona3:
            lista11= zona3.copy()
            lista11.remove(posicion)
            for i in lista11:
                if caracter == tableroLogico[i]:
                    validez=False
        if posicion in zona4:
            lista12= zona4.copy()
            lista12.remove(posicion)
            for i in lista12:
                if caracter == tableroLogico[i]:
                    validez=False

        return validez
    else: 
        print("el caracter no es valido ")
        return False

    
if __name__== "__main__":
    tablero = obtenerTableroLogico()
    tableroNuevo = actualizarTableroLogico(tablero, 0, 1)
    print(tableroNuevo)
    ganador =  determinarSiGano(tableroNuevo)
    print(ganador)

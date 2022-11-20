import interfaz
import logica   

interfaz.explicarJuego()
tableroJuego = logica.obtenerTableroLogico()
tableroJuego = interfaz.crearPistas(tableroJuego)
posibleGanador = logica.determinarSiGano(tableroJuego)

while posibleGanador == False:
    posicion = int(input("   Ingrese posicion a llenar: "))
    caracter = int(input("ingrese el numero con el que llenar la posicion:  "))
    if logica.determinarError(tableroJuego,posicion, caracter):
        tableroJuego = logica.actualizarTableroLogico(tableroJuego, posicion, caracter)
    else: print("la posicion ingresada no es valida")
    interfaz.dibujarTablero(tableroJuego)
    posibleGanador = logica.determinarSiGano(tableroJuego)
    if posibleGanador :
        print("Felicidades!!!! ha ganado el juego ")
        break
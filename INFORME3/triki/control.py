import interfaz
import logica

interfaz.explicarJuego()
tableroJuego= logica.obtenerTableroLogico()

for turno in ["X","O","X","O","X","O","X","O","X"]:
    print("\nTurno jugador: ", turno)
    if turno == "X":
        posicion= int(input("  Ingrese posicion de juego:  "))
        if logica.determinarPosicionOcupada(tableroJuego, posicion)== True:
            tableroLogico= logica.actualizarTableroLogico(tableroJuego, posicion, turno)
            interfaz.dibujarTablero(tableroJuego)
            posibleGanador=logica.determinarGanador(tableroJuego)
            if posibleGanador in ["X","O"]:
                print("Felicidades ha ganado el juego jugador ", turno)
                break
        else:
            print("la posicion ingresada no es valida ")
    else:
        import random 
        posicion= random.choice(logica.tableroFaltante(tableroJuego))
        if logica.determinarPosicionOcupada(tableroJuego, posicion)== True:
            tableroLogico= logica.actualizarTableroLogico(tableroJuego, posicion, turno)
            interfaz.dibujarTablero(tableroJuego)
            posibleGanador=logica.determinarGanador(tableroJuego)
            if posibleGanador in ["X","O"]:
                print("Felicidades ha ganado el juego jugador ", turno)
                break
        else:
            print("la posicion ingresada no es valida ")


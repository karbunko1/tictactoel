import os


class Tools():
    @staticmethod
    def clearScreen():
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")


class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]

    def display(self):
        print("\n     ")
        print("%s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print("%s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print("%s | %s | %s " % (self.cells[7], self.cells[8], self.cells[9]))

    def update_cell(self, cell_no, player):
        self.cells[cell_no] = player

    def refresh_screen(self):
        Tools.clearScreen()
        self.display()

    def space_check(self, position):
        return self.cells[position] == " "


class Jugador:

    def __init__(self):
        pass


    def pedirJugadaJugador(self, token, board ):
        try:
            choice = int(input(f"\n[{ token }] Elije del 1 - 9. > "))
            # while not self.board.space_check(choice):
            #    self.juega()
            
        except (ValueError, IndexError):
            print("\n       Numero invalido.")
            choice = self.pedirJugadaJugador(token, board)

        if not board.space_check(choice):
            print("\n Esa casilla ya esta usada")
            choice = self.pedirJugadaJugador(token, board)

        return choice

class Juego():

    def __init__(self):
        Tools.clearScreen()
        self.board = Board()
        self.jugador = Jugador()

    def juega(self):
        self.board.refresh_screen()
        while True:
            self.ejecutaTurno('X')
            self.ejecutaTurno('O')


    def ejecutaTurno(self, token):
        choice = self.jugador.pedirJugadaJugador(token, self.board)
        self.board.update_cell(choice, token)
        self.board.refresh_screen()

juego = Juego()
juego.juega()

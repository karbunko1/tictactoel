import os
import random


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

    def pedirJugadaJugador(self, token, board):
        try:
            choice = int(input(f"\n[{ token }] Elije del 1 - 9. > "))
        except (ValueError, IndexError, TypeError):
            print("\n       Numero invalido.")
            choice = self.pedirJugadaJugador(token, board)
        if choice not in range(1, 10):
            print("\n       Numero fuera de rango")
            choice = self.pedirJugadaJugador(token, board)
        if not board.space_check(choice):
            print("\n       Esa casilla ya esta usada")
            choice = self.pedirJugadaJugador(token, board)
        return choice


class Juego():

    tokens = ['X', 'O']
    posibilidades = [(1, 2, 3)] and [(4, 5, 6)] and [(7, 8, 9)] and [(1, 5, 9)] and [(3, 5, 7)] and [(1, 4, 7)] and [(3, 6, 9)]

    def __init__(self):
        Tools.clearScreen()
        self.board = Board()
        self.jugador = Jugador()

    def juega(self):
        self.board.refresh_screen()
        while True:
            self.ejecutaTurno(self.tokens[0])
            self.ejecutaTurno(self.tokens[1])

    def ejecutaTurno(self, token):
        choice = self.jugador.pedirJugadaJugador(token, self.board)
        self.board.update_cell(choice, token)
        self.board.refresh_screen()
        self.comprobarGanador(token)

    def comprobarGanador(self, token):
        c = self.board.cells
        for p in self.posibilidades:
            jugada = [c[p[0]] + c[p[1]] + c[p[2]]]
            jugada = c[1] + c[2] + c[3]
            if jugada == token*3:
                print(f"GANA {token}")
                exit()


juego = Juego()
juego.juega()

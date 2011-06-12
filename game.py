#!/usr/bin/env python

from chesslib import board
from chesslib import boardgui
import os

if os.path.exists("state.fen"):
    with open("state.fen") as save:
        board.init()
        board.load(save.read())
else:
    board.init()
boardgui.display()

## Text Mode

#os.system("clear")
#board.init()
#board.unicode_representation()

def move(coord):
    board.move(coord[0:2], coord[2:4])
    os.system("clear")
    board.unicode_representation()

def render():
    os.system("clear")
    board.unicode_representation()
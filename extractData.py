# exctractData.py
# coding=utf8
# -----------------------
# Esta clase se encarga de extraer los datos de la partida y guardarlos en
# un array para manipularlos

from sacarFilas import *
from saveData import *
from refuerzo import *
import os.path
from game import Actions
import random

datos = []
fantasmas = []

""" Esta funcion nos devolvera la posicion de la tabla Q segun el estado de
    partida en el que nos encontramos"""


def extract(self, gamestate, nearGhostParam):
    """ Aquí creamos los atributos para saber si un movimiento esta
        disponible o no """
    north = 0
    east = 0
    south = 0
    west = 0
    for i in gamestate.getLegalPacmanActions():
        if i == 'North':
            north = 1
        if i == 'East':
            east = 1
        if i == 'South':
            south = 1
        if i == 'West':
            west = 1

    """ Aqui vamos a ver que movimiento tendrá que realizar el Pac-Man
        para alcanzar el fantasma """
    bestMove = None
    distMove = None

    for action in [a for a in gamestate.getLegalPacmanActions()]:
        """ Aqui se calcula la posicion tomada una accion """
        nuevaposicion = Actions.getSuccessor(gamestate.data.agentStates[0].getPosition(), action)
        """ La distancia entre la posicion al realizar la accion y
            el fantasma """
        distancia = self.distancer.getDistance(nuevaposicion, nearGhostParam[4])
        if distMove is None or distancia < distMove:
            bestMove = action
            distMove = distancia

    """ Vamos a discretizar las distancias al fantasma
        Para ello vamos a hacer cuatro grupos:
            - 1: Menor a 3
            - 2: Menor a 8
            - 3: Menor a 15
            - 4: Mayor de 15 """
    gDist = None
    if nearGhostParam[1] <= 3:
        gDist = 1
    elif nearGhostParam[1] > 3 and nearGhostParam[1] <= 8:
        gDist = 2
    elif nearGhostParam[1] > 8 and nearGhostParam[1] <= 15:
        gDist = 3
    else:
        gDist = 4

    """ En este punto vamos a sacar la fila de la tabla q que corresponde """
    fila = sacarFila(north, south, east, west, bestMove, gDist)

    """ Guardamos el estado de la partida """
    estadoPartida = [north, south, east, west, bestMove, gDist]

    """ También sacamos el número de fantasmas vivos y muertos de los
        turnos """
    nFant = 4
    if gamestate.livingGhosts[1] is False:
        nFant = nFant - 1
    if gamestate.livingGhosts[2] is False:
        nFant = nFant - 1
    if gamestate.livingGhosts[3] is False:
        nFant = nFant - 1
    if gamestate.livingGhosts[4] is False:
        nFant = nFant - 1

    """ Guardamos la accion realizada """
    movimiento = str(gamestate.data.agentStates[0].getDirection())
    if movimiento == "Stop":
        sel = random.choice(range(4))
        if sel == 0:
            movimiento = "North"
        if sel == 1:
            movimiento = "East"
        if sel == 2:
            movimiento = "South"
        if sel == 3:
            movimiento = "West"

    """ Guardamos la informacion """
    fantasmas.append(nFant)
    datos.append(estadoPartida)
    refuerzo = 0

    if len(datos) >= 2:
        """ Calculamos el refuerzo """
        refuerzo = calcRefuerzo(self, fantasmas, datos, movimiento)
        print refuerzo

        """ Llamamos a saveData """
        saveData(datos, movimiento, refuerzo)

        """ Eliminamos el turno anterior despues de haberlo utilizado y pasar
            al siguiente """
        datos.pop(0)
        fantasmas.pop(0)

    return fila

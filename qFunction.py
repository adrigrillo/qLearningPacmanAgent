# qFunction.py
# coding=utf8
# -----------------------
# Esta clase se encarga de extraer los datos de la partida y guardarlos en
# un array para manipularlos
import math
from tableOperators import *
from extractData import *


def calculateFunction(alpha, gamma, estadoAnt, estado, refuerzo, accion):
    result = 0
    """ Devuelve en número la accion realizada """
    actionRealizada = actionConverter(accion)
    """ Q valor del estado del que transitamos """
    qValueAnt = computeQValueFromValues(estadoAnt, actionRealizada)
    """ Q valor maximo del estado al que transitamos """
    qValue = maxQValor(estado)
    """ Calculo del resultado """
    result = ((1 - alpha) * float(qValueAnt)) + (alpha * float(refuerzo + (gamma * float(qValue))))
    return result

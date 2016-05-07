# qFunction.py
# coding=utf8
# -----------------------
# Esta clase se encarga de extraer los datos de la partida y guardarlos en
# un array para manipularlos
import math
from tableOperators import *
from extractData import calcRefuerzo


def calculateFunction(alpha, gamma, estadoAnt, estado, accion):
    result = 0
    action = actionConverter(accion)
    qValueAnt = computeQValueFromValues(estado, accion)
    qValue = computeQValueFromValues(estado, accion)
    result = ((1 - alpha) * qValue) + alpha *
    return result

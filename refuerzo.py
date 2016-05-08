# Refuerzo.py
# coding=utf8
# -----------------------
# Esta es la función que se encarga de dar el refuerzo tras recibir la
# información de la jugada


def calcRefuerzo(fantasmas, datos, movimiento):
    refuerzo = 0
    """ Normalizamos las distancias """
    gDist = None
    if fantasmas[0][1] <= 3:
        gDist = 1
    if fantasmas[0][1] > 3 and fantasmas[0][1] <= 8:
        gDist = 2
    if fantasmas[0][1] > 8 and fantasmas[0][1] <= 15:
        gDist = 3
    if fantasmas[0][1] >= 15:
        gDist = 4

    gDistAct = None
    if fantasmas[1][1] <= 3:
        gDistAct = 1
    if fantasmas[1][1] > 3 and fantasmas[1][1] <= 8:
        gDistAct = 2
    if fantasmas[1][1] > 8 and fantasmas[1][1] <= 15:
        gDistAct = 3
    if fantasmas[1][1] >= 15:
        gDistAct = 4

    if fantasmas[0][0] > fantasmas[1][0]:
        refuerzo = 100
    elif movimiento is 'North' and datos[0][0] == 0:
        refuerzo = -100
    elif movimiento is 'South' and datos[0][1] == 0:
        refuerzo = -100
    elif movimiento is 'East' and datos[0][2] == 0:
        refuerzo = -100
    elif movimiento is 'West' and datos[0][3] == 0:
        refuerzo = -100
    elif gDist > gDistAct:
        refuerzo = 1
    else:
        refuerzo = -1
    return refuerzo

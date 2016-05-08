# Refuerzo.py
# coding=utf8
# -----------------------
# Esta es la función que se encarga de dar el refuerzo tras recibir la
# información de la jugada


def calcRefuerzo(fantasmas, datos, movimiento):
    refuerzo = 0
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

    elif fantasmas[0][1] > fantasmas[1][1]:
        refuerzo = 1
    else:
        refuerzo = 0
    return refuerzo

# Refuerzo.py
# -----------------------
# Esta es la función que se encarga de dar el refuerzo tras recibir la
# información de la jugada


def calcRefuerzo(self, fantasmas, datos, movimiento):
    refuerzo = 0
    print datos[0][5]
    print datos[1][5]
    if fantasmas[0] > fantasmas[1]:
        refuerzo = 100
    elif movimiento is 'North' and datos[0][0] == 0:
        refuerzo = -100
    elif movimiento is 'South' and datos[0][1] == 0:
        refuerzo = -100
    elif movimiento is 'East' and datos[0][2] == 0:
        refuerzo = -100
    elif movimiento is 'West' and datos[0][3] == 0:
        refuerzo = -100
    elif datos[0][5] > datos[1][5]:
        refuerzo = 1
    else:
        refuerzo = 0
    return refuerzo
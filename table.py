# ESTA CLASE ES PARA BORRAR
# Aqui estan los metodos que escriben en la tabla y leen

import json


def creator(estados, acciones):
    """ Lo primero sera crear la matriz llena de 0 """
    ejeX = []
    ejeY = [0, 0, 0, 0]

    for i in range(estados):
        ejeX.append(ejeY)

    """ Pasamos a abrir el archivo para guardar la matriz """
    f = open("QTable.json", "w")
    json.dump(ejeX, f)
    f.close()


def readQtable():
    f = open("QTable.json")
    matriz = json.load(f)
    f.close()
    return matriz


def writeQtable(qtable):
    f = open("QTable.json", "w")
    json.dump(qtable, f)
    f.close()

matriz = readQtable()
print matriz[0][0]

# tableOperators.py
# coding=utf8
# -------
# Aqui estan los metodos que crean, escriben y leen en la tabla Q
# Para simplificar el lector y el escritor de las tablasQ en el programa
# decidimos usar archivos JSON para guardar las tablas Q del juego.
# Usaremos una matriz de dos dimensiones donde el primer [] indicará
# el estado en el que se encuentra el Pac-Man
# La segunda [] será una lista con los Q valores para las diferentes acciones
# disponibles de forma que las posiciones de la lista significarán:
#   - Posición 0 --> north
#   - Posición 1 --> south
#   - Posición 2 --> east
#   - Posición 3 --> west
import json
import random


# Este metodo será el que cree la tablaQ que se guarde en un fichero
def creator(estados):
    """ Lo primero sera crear la matriz llena de 0 """
    ejeX = []
    ejeY = [0, 0, 0, 0]

    for i in range(estados):
        ejeX.append(ejeY)

    """ Pasamos a abrir el archivo para guardar la matriz """
    f = open("QTable.json", "w")
    json.dump(ejeX, f)
    f.close()
    return 2


# Este metodo será el que lea la tablaQ que se guarde en un fichero
def readQtable():
    f = open("QTable.json")
    matriz = json.load(f)
    f.close()
    return matriz


# Este metodo será el que escriba la tablaQ recibida por parametro
def writeQtable(qtable):
    f = open("QTable.json", "w")
    json.dump(qtable, f)
    f.close()
    return 1


# Metodo que devuelve el Q valor de un estado y accion determinada
def computeQValueFromValues(state, action):
    """ Obtenemos el Q valor de ese estado y esa accion """
    table = readQtable()
    print state, action
    valor = table[state][action]
    print valor
    return valor


# Metodo que devuelve la accion que maximiza el Q valor de la acción
def computeActionFromValues(state):
    """
      The policy is the best action in the given state
      according to the values currently stored in self.values.
      You may break ties any way you see fit.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return None.
    """
    """ Leemos la tablaQ actual """
    table = readQtable()
    """ Obtenemos los valores de la tablaQ para el estado actual """
    valores = table[state]
    """ Sacamos el maximo """
    maximo = max(valores)
    """ Sacamos la posicion en la que estaba de la lista de Q valores
            para saber que accion es la que maximiza """
    acciones = []
    for i in range(len(valores)):
        if valores[i] == maximo:
            acciones.append(i)
    index = random.randint(0, (len(acciones)-1))
    accion = acciones[index]
    action = -1
    if accion == 0:
        action = "North"
    if accion == 1:
        action = "South"
    if accion == 2:
        action = "East"
    if accion == 3:
        action = "West"
    """ Devolvemos el movimiento """
    return action


# Metodo que devuelve la accion que maximiza el Q valor de la acción
def maxQValor(state):
    """ Leemos la tablaQ actual """
    table = readQtable()
    """ Obtenemos los valores de la tablaQ para el estado actual """
    valores = table[state]
    """ Sacamos el maximo """
    maximo = max(valores)
    """ Sacamos la posicion en la que estaba de la lista de Q valores
            para saber que accion es la que maximiza """
    return maximo

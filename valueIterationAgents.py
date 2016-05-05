# valueIterationAgents.py
# -----------------------


import mdp
import util
import json
from learningAgents import ValueEstimationAgent


class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount=0.9, iterations=100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        """ Construimos la tablaQ al leerla """
        tableQ = readQtable()

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        """ Obtenemos el valor numerico de la accion para nuestro sistema """
        accion = str(action)
        if accion is "north":
            accion = 0
        elif accion is "south":
            accion = 1
        elif accion is "east":
            accion = 2
        else:
            accion = 3

        """ Obtenemos el Q valor de ese estado y esa accion """
        table = readQtable()
        valor = table[state[0]][state[1]][accion]
        return valor

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        """ Comprobamos que no es un estado final """
        if state is not "TERMINAL_STATE":
            """ Leemos la tablaQ actual """
            table = readQtable()
            """ Obtenemos los valores de la tablaQ para el estado actual """
            valores = table[state[0]][state[1]]
            """ Sacamos el maximo """
            maximo = max(valores)
            """ Sacamos la posicion en la que estaba de la lista de Q valores
                para saber que accion es la que maximiza """
            accion = valores.index(maximo)
            if accion == 0:
                accion = "north"
            elif accion == 1:
                accion = "south"
            elif accion == 2:
                accion = "east"
            else:
                accion = "west"
            """ Devolvemos el movimiento """
            return accion
        else:
            """ Si el estado es final """
            return None

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

    def readQtable():
        f = open("QTable.json")
        matriz = json.load(f)
        f.close()
        return matriz

    def writeQtable(qtable):
        f = open("QTable.json", "w")
        json.dump(qtable, f)
        f.close()

# bustersAgents.py
# coding=utf8
# ----------------

import util
from game import Agent
from game import Directions
from keyboardAgents import KeyboardAgent
import math
import inference
import busters


class NullGraphics:
    "Placeholder for graphics"
    def initialize(self, state, isBlue = False):
        pass

    def update(self, state):
        pass

    def pause(self):
        pass

    def draw(self, state):
        pass

    def updateDistributions(self, dist):
        pass

    def finish(self):
        pass


class KeyboardInference(inference.InferenceModule):
    """
    Basic inference module for use with the keyboard.
    """
    def initializeUniformly(self, gameState):
        "Begin with a uniform distribution over ghost positions."
        self.beliefs = util.Counter()
        for p in self.legalPositions: self.beliefs[p] = 1.0
        self.beliefs.normalize()

    def observe(self, observation, gameState):
        noisyDistance = observation
        emissionModel = busters.getObservationDistribution(noisyDistance)
        pacmanPosition = gameState.getPacmanPosition()
        allPossible = util.Counter()
        for p in self.legalPositions:
            trueDistance = util.manhattanDistance(p, pacmanPosition)
            if emissionModel[trueDistance] > 0:
                allPossible[p] = 1.0
        allPossible.normalize()
        self.beliefs = allPossible

    def elapseTime(self, gameState):
        pass

    def getBeliefDistribution(self):
        return self.beliefs


class BustersAgent:
    "An agent that tracks and displays its beliefs about ghost positions."

    def __init__( self, index = 0, inference = "ExactInference", ghostAgents = None, observeEnable = True, elapseTimeEnable = True):
        inferenceType = util.lookup(inference, globals())
        self.inferenceModules = [inferenceType(a) for a in ghostAgents]
        self.observeEnable = observeEnable
        self.elapseTimeEnable = elapseTimeEnable

    def registerInitialState(self, gameState):
        "Initializes beliefs and inference modules"
        import __main__
        self.display = __main__._display
        for inference in self.inferenceModules:
            inference.initialize(gameState)
        self.ghostBeliefs = [inf.getBeliefDistribution() for inf in self.inferenceModules]
        self.firstMove = True

    def observationFunction(self, gameState):
        "Removes the ghost states from the gameState"
        agents = gameState.data.agentStates
        gameState.data.agentStates = agents
        """ Creamos parametro global que imprime ciertos parámetros
            sobre el fantasma más cercano:
            0: Fantasma a por el que va
            1: Distancia manhattan al fantasma
            2: Distancia en eje x con el fantasma. + al oeste - al este
            3: Distancia en eje x con el fantasma. + al norte - al sur """
        global nearGhostParam
        nearGhostParam = [0, 0, 0, 0, 0]
        nearDist = None
        nearGhost = 1
        nearX = 0
        nearY = 0
        posGhost = None

        """ Sacamos los fantasmas para solo calcular la distancia con estos """
        ghostDead = []
        if gameState.livingGhosts[1] is True:
            ghostDead.append(1)
        if gameState.livingGhosts[2] is True:
            ghostDead.append(2)
        if gameState.livingGhosts[3] is True:
            ghostDead.append(3)
        if gameState.livingGhosts[4] is True:
            ghostDead.append(4)
        """Sacamos la posición del fantasma más cercano"""
        for i in ghostDead:
            x = gameState.data.agentStates[i].getPosition()[0] - gameState.data.agentStates[0].getPosition()[0]
            y = gameState.data.agentStates[i].getPosition()[1] - gameState.data.agentStates[0].getPosition()[1]
            res = math.sqrt(pow(abs(x), 2) + pow(abs(y), 2))
            if nearDist is None or nearDist > res:
                nearDist = res
                nearGhost = i
                nearX = x
                nearY = y
                posGhost = gameState.data.agentStates[i].getPosition()

        nearGhostParam[0] = nearGhost
        nearGhostParam[1] = nearDist
        nearGhostParam[2] = nearX
        nearGhostParam[3] = nearY
        nearGhostParam[4] = posGhost
        return gameState

    def getAction(self, gameState):
        "Updates beliefs, then chooses an action based on updated beliefs."
        for index, inf in enumerate(self.inferenceModules):
            if not self.firstMove and self.elapseTimeEnable:
                inf.elapseTime(gameState)
            self.firstMove = False
            if self.observeEnable:
                inf.observeState(gameState)
            self.ghostBeliefs[index] = inf.getBeliefDistribution()
        self.display.updateDistributions(self.ghostBeliefs)
        return self.chooseAction(gameState)

    def chooseAction(self, gameState):
        "By default, a BustersAgent just stops.  This should be overridden."
        return Directions.STOP


class BustersKeyboardAgent(BustersAgent, KeyboardAgent):
    """An agent controlled by the keyboard that displays beliefs about ghost
        positions."""

    def __init__(self, index=0, inference="KeyboardInference", ghostAgents=None):
        KeyboardAgent.__init__(self, index)
        BustersAgent.__init__(self, index, inference, ghostAgents)

    def getAction(self, gameState):
        return BustersAgent.getAction(self, gameState)

    def chooseAction(self, gameState):
        return KeyboardAgent.getAction(self, gameState)

from distanceCalculator import Distancer
from game import Actions
from game import Directions
import random, sys

'''Random PacMan Agent'''
class RandomPAgent(BustersAgent):

    def registerInitialState(self, gameState):
        BustersAgent.registerInitialState(self, gameState)
        self.distancer = Distancer(gameState.data.layout, False)

    ''' Example of counting something'''
    def countFood(self, gameState):
        food = 0
        for width in gameState.data.food:
            for height in width:
                if(height == True):
                    food = food + 1
        return food

    ''' Print the layout'''
    """def printGrid(self, gameState):
        table = ""
        ##print(gameState.data.layout) ## Print by terminal
        for x in range(gameState.data.layout.width):
            for y in range(gameState.data.layout.height):
                food, walls = gameState.data.food, gameState.data.layout.walls
                table = table + gameState.data._foodWallStr(food[x][y], walls[x][y]) + ","
        table = table[:-1]
        return table"""

    def printLineData(self,gameState):

        '''Observations of the state

        print(str(gameState.livingGhosts))
        print(gameState.data.agentStates[0])
        print(gameState.getNumFood())
        print (gameState.getCapsules())
        width, height = gameState.data.layout.width, gameState.data.layout.height
        print(width, height)
        print(gameState.data.ghostDistances)
        print(gameState.data.layout)'''

        '''END Observations of the state'''

        print gameState

        """weka_line = ""
        for i in gameState.livingGhosts:
            weka_line = weka_line + str(i) + ","
        weka_line = weka_line + str(gameState.getNumFood()) + ","
        for i in gameState.getCapsules():
            weka_line = weka_line + str(i[0]) + "," + str(i[1]) + ","
        for i in gameState.data.ghostDistances:
            weka_line = weka_line + str(i) + ","
        weka_line = weka_line + str(gameState.data.score) + "," +\
        str(len(gameState.data.capsules))  + "," + str(self.countFood(gameState)) +\
        "," + str(gameState.data.agentStates[0].configuration.pos[0]) + "," +\
        str(gameState.data.agentStates[0].configuration.pos[0])  +\
        "," + str(gameState.data.agentStates[0].scaredTimer) + "," +\
        self.printGrid(gameState) + "," +\
        str(gameState.data.agentStates[0].numReturned) + "," +\
        str(gameState.data.agentStates[0].getPosition()[0]) + "," +\
        str(gameState.data.agentStates[0].getPosition()[1])+ "," +\
        str(gameState.data.agentStates[0].numCarrying)+ "," +\
        str(gameState.data.agentStates[0].getDirection())
        print(weka_line)"""


    def chooseAction(self, gameState):
        move = Directions.STOP
        legal = gameState.getLegalActions(0) ##Legal position from the pacman
        move_random = random.randint(0, 3)
        self.printLineData(gameState)
        if   ( move_random == 0 ) and Directions.WEST in legal:  move = Directions.WEST
        if   ( move_random == 1 ) and Directions.EAST in legal: move = Directions.EAST
        if   ( move_random == 2 ) and Directions.NORTH in legal:   move = Directions.NORTH
        if   ( move_random == 3 ) and Directions.SOUTH in legal: move = Directions.SOUTH
        extract(self, gameState, nearGhostParam)
        return move

"""




                        Q LEARNING AGENT







"""
from extractData import *
from tableOperators import *
from qFunction import *


class AgentQLearning(BustersAgent):
    "An agent that charges the closest ghost."

    def registerInitialState(self, gameState):
        "Pre-computes the distance between every two points."
        BustersAgent.registerInitialState(self, gameState)
        self.distancer = Distancer(gameState.data.layout, False)

    def chooseAction(self, gameState):
        """ En este punto iniciamos el agente, leemos la tabla q guardada
            en el archivo"""
        qtable = readQtable()
        """ En este punto obtenemos la fila de la tabla q al que pertenece
            el estado y el refuerzo de la accion realizada
                - datos[0]: fila del estado anterior en la tablaQ
                - datos[1]: fila del estado actual en la tablaQ
                - datos[2]: refuerzo
        """
        datos = extract(self, gameState, nearGhostParam)
        """ Ahora calculamos el siguiente movimiento """
        movimiento = computeActionFromValues(datos[1])
        movRealizar = None
        if movimiento == "North":
            movRealizar = Directions.NORTH
        elif movimiento == "South":
            movRealizar = Directions.SOUTH
        elif movimiento == "East":
            movRealizar = Directions.EAST
        else:
            movRealizar = Directions.WEST

        """ Miramos si el siguiente movimiento es legal, para dar un refuerzo
            negativo si no es asi """
        qValor = 0
        legal = 0
        for i in gameState.getLegalPacmanActions():
            if movimiento is i:
                legal = 1

        if legal == 1:
            """ Sacamos el q valor del estado del que transitamos """
            qValor = calculateFunction(0.7, 0.9, datos[0], datos[1], datos[2], str(gameState.data.agentStates[0].getDirection()))
            accion = actionConverter(str(gameState.data.agentStates[0].getDirection()))
            qtable[datos[0]][accion] = qValor
            writeQtable(qtable)
        else:
            print "Es ilegal"
            qValor = calculateFunction(0.7, 0.9, datos[1], datos[1], -100, str(movRealizar))
            accion = actionConverter(str(movRealizar))
            qtable[datos[1]][accion] = qValor
            writeQtable(qtable)

        return movRealizar



"""







    A PARTIR DE AQUI NO IMPORTA








"""
from learningAgents import ReinforcementAgent

"""
      Q-Learning Agent

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
"""

class QLearningAgent(BustersAgent, ReinforcementAgent):
    "An agent that charges the closest ghost."
    """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:

        QTable   - QTable
        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """

    def __init__(self, index=0, inference="ExactInference", ghostAgents=None, observeEnable=True, elapseTimeEnable=True):
        inferenceType = util.lookup(inference, globals())
        self.inferenceModules = [inferenceType(a) for a in ghostAgents]
        self.observeEnable = observeEnable
        self.elapseTimeEnable = elapseTimeEnable

    def registerInitialState(self, gameState):
        "Pre-computes the distance between every two points."
        BustersAgent.registerInitialState(self, gameState)
        self.distancer = Distancer(gameState.data.layout, False)

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def chooseAction(self, gameState):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        util.raiseNotDefined()

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.chooseAction(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.chooseAction(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, **args):
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.chooseAction(self,state)
        self.doAction(state,action)
        return action
    def chooseAction(self, gameState):
        action = QLearningAgent.chooseAction(self,gameState)
        return action

class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent

       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """

        util.raiseNotDefined()

    def update(self, state, action, nextState, reward):
        """
           Should update your weights basedPaca on transition
        """
        "*** YOUR CODE HERE ***"
        feats = self.featExtractor.getFeatures(state, action)
        for f in feats:
          self.weights[f] = self.weights[f] + self.alpha * feats[f]*((reward + self.discount * self.computeValueFromQValues(nextState)) - self.getQValue(state, action))

        # util.raiseNotDefined()

    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            pass

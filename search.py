# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util
from collections import namedtuple

node = namedtuple("node", "state, parent, action, pathCost")


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 85].

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].

    Use the 'node' data type defined at the beginning. As an example, the root node can be created
    like so: root = node(problem.getStartState(), None, None, 0), where the parent node and the action
    that led to the root node are both 'None', meaning nil.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    from game import Directions

    open = util.Stack()
    closed = []
    moves = []

    root = node(problem.getStartState(), None, None, 0)

    open.push(root)

    while not open.isEmpty():
        curNode = open.pop()

        if problem.isGoalState(curNode.state):

            while curNode.parent != None:
                moves.insert(0, {
                    'North': Directions.NORTH,
                    'South': Directions.SOUTH,
                    'East' : Directions.EAST,
                    'West' : Directions.WEST,
                }[curNode.action])

                curNode = curNode.parent

            return moves

        else:
            children = problem.getSuccessors(curNode.state)
            closed.append(curNode)

            if len(children) > 0:
                for child in range(len(children)):

                    curChild = node(children[child][0], curNode, children[child][1], children[child][2])
                    inClosed = False

                    for i in range(len(closed)):
                        if curChild.state == closed[i].state:
                            inClosed = True
                            break

                    if not inClosed:
                        open.push(curChild)

    print "Unable to find path!"

    # util.raiseNotDefined()


def breadthFirstSearch(problem):
    "Search the shallowest nodes in the search tree first. [p 81]"

    from game import Directions

    open = util.Queue()
    closed = []
    moves = []

    root = node(problem.getStartState(), None, None, 0)

    open.push(root)

    while not open.isEmpty():
        curNode = open.pop()

        if problem.isGoalState(curNode.state):

            while curNode.parent != None:
                moves.insert(0, {
                    'North': Directions.NORTH,
                    'South': Directions.SOUTH,
                    'East' : Directions.EAST,
                    'West' : Directions.WEST,
                }[curNode.action])

                curNode = curNode.parent

            return moves

        else:
            children = problem.getSuccessors(curNode.state)
            closed.append(curNode)

            if len(children) > 0:
                for child in range(len(children)):

                    curChild = node(children[child][0], curNode, children[child][1], children[child][2])
                    inClosed = False

                    for i in range(len(closed)):
                        if curChild.state == closed[i].state:
                            inClosed = True
                            break

                    if not inClosed:
                        open.push(curChild)

    print "Unable to find path!"

    #util.raiseNotDefined()


def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."


    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

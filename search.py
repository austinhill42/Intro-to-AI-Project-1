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

    opened = util.Stack()  # Use a stack to visit nodes
    closed = []  # List of visited nodes
    moves = []  # List of moves to return once goal is found

    opened.push(node(problem.getStartState(), None, None, 0))  # Push root onto the stack

    while not opened.isEmpty():
        current = opened.pop()  # Visit the node at the top of the stack

        if problem.isGoalState(current.state):  # At goal state

            # Starting at current node and not exceeding root, insert the node
            # action into moves at beginning for correct order, and then return moves
            while current.parent is not None:
                moves.insert(0, current.action)
                current = current.parent

            return moves

        else:  # Not at goal state
            children = problem.getSuccessors(current.state)  # Get list of children
            closed.append(current)  # Add current node to visited list

            if len(children) > 0:  # Children exist
                """
                For the medium maze, adding successors in reverse order using
                    for i in reversed(range(len(children)))
                results in a length of 246 while the loop below results in a length of 146,
                so I chose to go with the latter
                """
                for i in range(len(children)):

                    child = node(children[i][0], current, children[i][1],
                                 children[i][2])  # Create a node for each child
                    visited = False  # Reset visited

                    for j in range(len(closed)):  # Search for child in closed
                        if child.state == closed[j].state:
                            visited = True
                            break

                    if not visited:  # If not in closed, push child onto stack
                        opened.push(child)

    print "Unable to find path!"  # Either no path exists or open was somehow empty before one was found

    # util.raiseNotDefined()


def breadthFirstSearch(problem):
    "Search the shallowest nodes in the search tree first. [p 81]"

    opened = util.Queue()  # Use a queue to visit nodes
    closed = []  # List of visited nodes
    moves = []  # List of moves to return once goal is found

    opened.push(node(problem.getStartState(), None, None, 0))  # Push root into the queue

    while not opened.isEmpty():
        current = opened.pop()  # Visit the node at the front of the queue

        if problem.isGoalState(current.state):  # At goal state

            # Starting at current node and not exceeding root, insert the node
            # action into moves at beginning for correct order, and then return moves
            while current.parent is not None:
                moves.insert(0, current.action)
                current = current.parent

            return moves

        else:  # Not at goal state
            children = problem.getSuccessors(current.state)  # Get list of children
            closed.append(current)  # Add current node to visited list

            if len(children) > 0:  # Children exist
                for i in range(len(children)):

                    child = node(children[i][0], current, children[i][1],
                                 children[i][2])  # Create a node for each child
                    visited = False  # Reset visited

                    for j in range(len(closed)):  # Search for child in closed
                        if child.state == closed[j].state:
                            visited = True
                            break

                    if not visited:  # If not in closed, push child into queue
                        opened.push(child)

    print "Unable to find path!"  # Either no path exists or open was somehow empty before one was found

    # util.raiseNotDefined()


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

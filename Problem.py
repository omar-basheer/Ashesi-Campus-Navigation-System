from Search import *

class Problem:
    """This class represents a generic Problem to be solved by search"""
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def __str__(self):
        return (type(self).__name__ + ": Initial State=" + str(self.initial_state) +
                ", Goal state=" + str(self.goal_state))

    def goal_test(self, state):
        return False

    def actions(self,state):
        return None

class CampusNavigationProb(Problem):
    """This class represents the problem of navigating the Ashesi University campus"""

    def __init__(self, initial_state, goal_state):
        super().__init__(initial_state,goal_state)
        self.map = initalize_map()
        self.pixel_dict = initalize_pixelDict()

    def goal_test(self, state):
        return (state == self.goal_state)

    def actions(self,state):
        neighbours = self.map.adjacency_list[state]
        successor_nodes = []
        #weight = []
        for i in range(len(neighbours)):
            landmark = neighbours[i]
            #transcost = neighbours[i].path_cost
            successor_nodes.append(landmark)
            #weight.append(transcost)

        return successor_nodes

    def display_prob(self):
        print("__CampusNavigationProblem__")
        print("Initial state=", self.initial_state)
        print("Goal state =", self.goal_state)























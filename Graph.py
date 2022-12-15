class Graph:
    """This class represents a graph instance. The graph is used to model paths between landmarks"""
    def __init__(self):
        self.adjacency_list = dict()

    def add_edge(self, start, goal, edge_cost, action=None):
        if start in self.adjacency_list.keys():
            node = Node(goal, path_cost=edge_cost, action=action)
            self.adjacency_list[start].append(node)

        else:
            node = Node(goal, path_cost=edge_cost, action=action)
            temp = [node]
            self.adjacency_list[start] = temp

class Node:
    """This class represents a node object"""

    def __init__(self, state, parent = None, action = None, path_cost = None):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __hash__(self):
        return self.state.__hash__()


    def __str__(self):
        tempStr = "Node with state=" + str(self.state)

        if (self.parent != None):
            tempStr += (", parent= " + str(self.parent.state) +
                        ", action=" + str(self.action) + ", path_cost="+
                        str(self.path_cost))

        return tempStr

    def __eq__(self, cur):
        return (isinstance(cur, Node) and self.state == cur.state)
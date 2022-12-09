import math
from Graph import *
from PriorityQueue import *
from Problem import *




def initalize_pixelDict():
    pixel_dictionary = dict()
    pixel_dictionary["Radichel Hall"] = (423.90, 1369.60)
    pixel_dictionary["Warren Library"] = (472.13, 1237.95)
    pixel_dictionary["Apt Hall"] = (552.40, 1252.50)
    pixel_dictionary["Jackson Hall"] = (517.50, 1379.70)
    pixel_dictionary["DataBank Foundation Hall"] = (585.90, 1338.10)
    pixel_dictionary["Ashesi Bookshop"] = (647.10, 1299.10)
    pixel_dictionary["King Engineering Building"] = (579.70, 1118.00)
    pixel_dictionary["Nutor Hall"] = (721.90, 1227.80)
    pixel_dictionary["Fab Lab"] = (543.77, 737.18)
    pixel_dictionary["Engineering Workshop"] = (653.81, 538.14)
    pixel_dictionary["The Hive"] = (864.70, 1242.80)
    pixel_dictionary["The Grill"] = (717.40, 1352.20)
    pixel_dictionary["Bliss Lounge"] = (712.30, 1490.17)
    pixel_dictionary["Natembea Health Centre"] = (584.72, 682.34)
    pixel_dictionary["Basketball Court"] = (740.20, 1517.30)
    pixel_dictionary["Volleyball Court"] = (1115.90, 1515.90)
    pixel_dictionary["Isolation Wards"] = (1264.50, 1743.30)
    pixel_dictionary["Archer Cornfield Courtyard"] = (350.30, 1203.50)
    pixel_dictionary["Founders Plaza"] = (466.10, 1412.90)
    pixel_dictionary["Collins Courtyard"] = (561.80, 1313.10)
    pixel_dictionary["Porters' Lodge"] = (871.40, 1499.40)
    pixel_dictionary["Thacher Arboretum"] = (354.20, 1209.70)
    pixel_dictionary["Sutherland Hall"] = (641.80, 1484.50)
    pixel_dictionary["Amu Hall"] = (253.61, 1467.40)
    pixel_dictionary["Mathaai Hall"] = (936.50, 1560.15)
    pixel_dictionary["Hall 2C"] = (1158.60, 1484.40)
    pixel_dictionary["Oteng Korankye II Hall"] = (644.70, 1596.70)
    pixel_dictionary["Sisulu Hall"] = (788.40, 613.00)
    pixel_dictionary["Tawiah Hall"] = (957.60, 1595.10)
    pixel_dictionary["Hall 2D"] = (1163.80, 1625.10)
    pixel_dictionary["Service Centre"] = (727.20, 464.60)
    pixel_dictionary["Staff Housing"] = (73.04, 1220.59)
    pixel_dictionary["Water Treatment Plant"] = (472.13, 1237.95)
    pixel_dictionary["Biodigester Plant"] = (1012.17, 1824.01)
    pixel_dictionary["Sports Centre"] = (930.40, 253.10)
    pixel_dictionary["University Checkpoint"] = (68.50, 1122.30)
    pixel_dictionary["Green Gate"] = (492.30, 1180.20)
    pixel_dictionary["Munchies"] = (472.13, 1237.95)

    return pixel_dictionary


def initalize_map():
    AshesiMap = Graph()

    AshesiMap.add_edge("Sports Centre", "Service Centre", 3, "From Sports Centre, go straight to the first building on your right")
    AshesiMap.add_edge("Sports Centre", "Engineering Workshop", 7)
    AshesiMap.add_edge("Sports Centre", "Natembea Health Centre", 10)
    AshesiMap.add_edge("Sports Centre", "Fab Lab", 13, "Go straight to the fourth building on your right")
    AshesiMap.add_edge("Sports Centre", "Thacher Arboretum", 20)
    AshesiMap.add_edge("Service Centre", "Engineering Workshop", 2)
    AshesiMap.add_edge("Service Centre", "Natembea Health Centre", 3)
    AshesiMap.add_edge("Service Centre", "Fab Lab", 5)
    AshesiMap.add_edge("Engineering Workshop", "Fab Lab", 4)
    AshesiMap.add_edge("Engineering Workshop", "Natembea Health Centre", 3)
    AshesiMap.add_edge("Natembea Health Centre", "Fab Lab", 1)
    AshesiMap.add_edge("Fab Lab", "King Engineering Building", 15, "Go straight and take the first left. Continue "
                                                                   "straight to the first buildng on your left")
    AshesiMap.add_edge("Fab Lab", "Green Gate", 10)
    AshesiMap.add_edge("Green Gate", "Warren Library", 2)
    AshesiMap.add_edge("Green Gate", "King Engineering Building", 5)
    AshesiMap.add_edge("King Engineering Building", "Nutor Hall", 2, "Go straight to the next building")
    AshesiMap.add_edge("Radichel Hall", "Warren Library", 5)
    AshesiMap.add_edge("Warren Library", "Apt Hall", 3)
    AshesiMap.add_edge("Radichel Hall", "Jackson Hall", 2)
    AshesiMap.add_edge("Jackson Hall", "Collins Courtyard", 2)
    AshesiMap.add_edge("Jackson Hall", "Founders Plaza", 2)
    AshesiMap.add_edge("Radichel Hall", "Founders Plaza", 2)
    AshesiMap.add_edge("Apt Hall", "Collins Courtyard", 1)
    AshesiMap.add_edge("Collins Courtyard", "DataBank Foundation Hall", 1)
    AshesiMap.add_edge("Collins Courtyard", "Ashesi Bookshop", 1)
    AshesiMap.add_edge("University Checkpoint", "Munchies", 25)
    AshesiMap.add_edge("University Checkpoint", "Staff Housing", 7)
    AshesiMap.add_edge("University Checkpoint", "Founders Plaza", 15)
    AshesiMap.add_edge("University Checkpoint", "Thacher Arboretum", 13)
    AshesiMap.add_edge("University Checkpoint", "Green Gate", 12)
    AshesiMap.add_edge("Nutor Hall", "The Hive", 2, "Turn left and go straight. Turn right and use the staircase up to the Hive.")

    AshesiMap.add_edge("Service Centre", "Sports Centre", 3)
    AshesiMap.add_edge("Engineering Workshop", "Sports Centre", 7)
    AshesiMap.add_edge("Natembea Health Centre", "Sports Centre", 10)
    AshesiMap.add_edge("Fab Lab", "Sports Centre", 13)
    AshesiMap.add_edge("Thacher Arboretum", "Sports Centre", 20)
    AshesiMap.add_edge("Engineering Workshop", "Service Centre", 2)
    AshesiMap.add_edge("Natembea Health Centre", "Service Centre", 3)
    AshesiMap.add_edge("Fab Lab", "Service Centre", 5)
    AshesiMap.add_edge("Fab Lab", "Engineering Workshop", 4)
    AshesiMap.add_edge("Natembea Health Centre", "Engineering Workshop", 3)
    AshesiMap.add_edge("Fab Lab", "Natembea Health Centre", 1)
    AshesiMap.add_edge("King Engineering Building", "Fab Lab", 15)
    AshesiMap.add_edge("Green Gate", "Fab Lab", 10)
    AshesiMap.add_edge("Warren Library", "Green Gate", 2)
    AshesiMap.add_edge("King Engineering Building", "Green Gate", 5)
    AshesiMap.add_edge("Nutor Hall", "King Engineering Building", 2)
    AshesiMap.add_edge("Warren Library", "Radichel Hall", 5)
    AshesiMap.add_edge("Apt Hall", "Warren Library", 3)
    AshesiMap.add_edge("Jackson Hall", "Radichel Hall", 2)
    AshesiMap.add_edge("Collins Courtyard", "Jackson Hall", 2)
    AshesiMap.add_edge("Founders Plaza", "Jackson Hall", 2)
    AshesiMap.add_edge("Founders Plaza", "Radichel Hall", 2)
    AshesiMap.add_edge("Collins Courtyard", "Apt Hall", 1)
    AshesiMap.add_edge("DataBank Foundation Hall", "Collins Courtyard", 1)
    AshesiMap.add_edge("Ashesi Bookshop", "Collins Courtyard", 1)
    AshesiMap.add_edge("Munchies", "University Checkpoint", 25)
    AshesiMap.add_edge("Staff Housing", "University Checkpoint", 7)
    AshesiMap.add_edge("Founders Plaza", "University Checkpoint", 15)
    AshesiMap.add_edge("Thacher Arboretum", "University Checkpoint", 13)
    AshesiMap.add_edge("Green Gate", "University Checkpoint", 12)
    AshesiMap.add_edge("The Hive", "Nutor Hall", 2)

    return AshesiMap


def heuristic(current_state, goal_state, pixel_dict):  # string current state and string goal state
    start_pixel = pixel_dict[current_state]
    goal_pixel = pixel_dict[goal_state]
    # each pixel is a tuple of x and y values
    start_x = start_pixel[0]
    start_y = start_pixel[1]
    goal_x = goal_pixel[0]
    goal_y = goal_pixel[1]
    x_squared = pow(goal_x - start_x, 2)
    y_squared = pow(goal_y - start_y, 2)
    heuristic = math.sqrt(x_squared + y_squared)
    return heuristic

def aStarSearch(problem):
    explored = set()
    predecessors = dict()
    transcost = dict()
    frontier = PriorityQueue()
    start = Node(problem.initial_state)
    print(start)
    transcost[start.state] = 0
    frontier.add(start)

    while frontier:
        node = frontier.pop()
        print("popped node: ", node)
        print("frontier: ", frontier)

        if (problem.goal_test(node.state)):
            print("Found a solution! ", node)
            path = solution_path(predecessors,problem.initial_state,problem.goal_state)
            #INCOMPLETE
            return path

        explored.add(node.state)
        print("explored: ", explored)
        successors = problem.actions(node.state)
        print("successors: ", successors)
        for i in range(len(successors)):
             child = successors[i]
             distance = successors[i].path_cost
             f_value = transcost[node.state] + distance + heuristic(child.state,problem.goal_state,problem.pixel_dict)
             frontier.add(child, priority= f_value)
             print("estimated overall cost: ", child.state, f_value)


             if child.state not in transcost or transcost[node.state] + distance  < transcost[child.state]:
                print("edgecost of successor?: ", distance)
                print("transcost to node?: ", transcost[node.state])
                transcost[child.state] = transcost[node.state] + distance
                print("now, transcost to node?: ", transcost[child.state])
                print("this one: ", child.state, transcost[child.state])
                predecessors[child.state] = node.state

        print("frontier: ", frontier)
        print()

    return None

def solution_path(predecessors, start, goal):
    path = [goal]
    while goal != start:
        goal = predecessors[goal]
        path.append(goal)
    return list(reversed(path))


if __name__ == "__main__":
    myProb = CampusNavigationProb("Munchies", "Sports Centre")
    myProb.display_prob()

    solution = aStarSearch(myProb)
    print(solution)

import customtkinter
import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
from Graph import *
from PriorityQueue import *
from Problem import *

image1 = cv2.imread('AerialView.jpg')

image = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)


def initalize_pixelDict():
    pixel_dictionary = dict()
    pixel_dictionary["Radichel Hall"] = (423.90, 1369.60)
    pixel_dictionary["Warren Library"] = (472.13, 1237.95)
    pixel_dictionary["Apt Hall"] = (552.40, 1252.50)
    pixel_dictionary["Jackson Hall"] = (517.50, 1379.70)
    pixel_dictionary["Databank Foundation Hall"] = (585.90, 1338.10)
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
    pixel_dictionary["Archer Cornfield"] = (350.30, 1203.50)
    pixel_dictionary["Founders Plaza"] = (466.10, 1412.90)
    #pixel_dictionary["Archer Cornfield"] = (561.80, 1313.10)
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


def initalize_aerial_coordinates():
    aerial_coordinates = dict()
    aerial_coordinates["Sports Centre-Service Centre"] = np.array([[(458, 151), (416, 196), (470, 240), (435, 278)]])
    aerial_coordinates["Service Centre-Sports Centre"] = np.array([[(435, 278), (470, 240), (416, 196), (458, 151)]])
    aerial_coordinates["Service Centre-Engineering Workshop"] = np.array([[(435, 278), (388, 334)]])
    aerial_coordinates["Engineering Workshop-Service Centre"] = np.array([[(388, 334), (435, 278)]])
    aerial_coordinates["Engineering Workshop-Natembea Health Centre"] = np.array([[(388, 334), (355, 378)]])
    aerial_coordinates["Natembea Health Centre-Engineering Workshop"] = np.array([[(355, 378), (388, 334)]])
    aerial_coordinates["Natembea Health Centre-Fab Lab"] = np.array([[(355, 378), (318, 420)]])
    aerial_coordinates["Fab Lab-Natembea Health Centre"] = np.array([[(318, 420), (355, 378)]])
    aerial_coordinates["Fab Lab-Green Gate"] = np.array([[(318, 420), (222, 606)]])
    aerial_coordinates["Green Gate-Fab Lab"] = np.array([[(222, 606), (318, 420)]])
    aerial_coordinates["Green Gate-King Engineering Building"] = np.array([[(222, 606), (278, 652), (308, 663)]])
    aerial_coordinates["King Engineering Building-Green Gate"] = np.array([[(308, 663), (278, 652), (222, 606)]])
    aerial_coordinates["Green Gate-Warren Library"] = np.array([[(222, 606), (278, 652), (270, 689)]])
    aerial_coordinates["Warren Library-Green Gate"] = np.array([[(270, 689), (278, 652), (222, 606)]])
    aerial_coordinates["King Engineering Building-Nutor Hall"] = np.array([[(308, 663), (390, 708)]])
    aerial_coordinates["Nutor Hall-King Engineering Building"] = np.array([[(390, 708), (308, 663)]])
    aerial_coordinates["Nutor Hall-The Hive"] = np.array([[(390, 708), (426, 720), (477, 724)]])
    aerial_coordinates["The Hive-Nutor Hall"] = np.array([[(477, 724), (426, 720), (390, 708)]])
    aerial_coordinates["Warren Library-Apt Hall"] = np.array([[(270, 689), (283, 706)]])
    aerial_coordinates["Apt Hall-Warren Library"] = np.array([[(283, 706), (270, 689)]])
    aerial_coordinates["Warren Library-Radichel Hall"] = np.array([[(270, 689), (218, 727), (243, 745)]])
    aerial_coordinates["Radichel Hall-Warren Library"] = np.array([[(243, 745), (218, 727), (270, 689)]])
    aerial_coordinates["Radichel Hall-Jackson Hall"] = np.array([[(245, 745), (269, 755), (276, 741)]])
    aerial_coordinates["Jackson Hall-Radichel Hall"] = np.array([[(276, 741), (269, 755), (245, 745)]])
    aerial_coordinates["Jackson Hall-Founders Plaza"] = np.array([[(276, 741), (256, 783)]])
    aerial_coordinates["Founders Plaza-Jackson Hall"] = np.array([[(256, 783), (276, 741)]])
    aerial_coordinates["Radichel Hall-Founders Plaza"] = np.array([[(243, 745), (270, 752), (256, 783)]])
    aerial_coordinates["Founders Plaza-Radichel Hall"] = np.array([[(256, 783), (270, 752), (243, 745)]])
    aerial_coordinates["Archer Cornfield-Apt Hall"] = np.array([[(261, 680), (286, 698)]])
    aerial_coordinates["Apt Hall-Archer Cornfield"] = np.array([[(286, 698), (261, 680)]])
    aerial_coordinates["Archer Cornfield-Databank Foundation Hall"] = np.array(
        [[(261, 680), (284, 701), (316, 715), (302, 733), (322, 746)]])
    aerial_coordinates["Databank Foundation Hall-Archer Cornfield"] = np.array(
        [[(322, 746), (302, 733), (316, 715), (284, 701), (261, 680)]])
    aerial_coordinates["Archer Cornfield-Ashesi Bookshop"] = np.array(
        [[(261, 680), (284, 701), (325, 713), (326, 708), (347, 715)]])
    aerial_coordinates["Ashesi Bookshop-Archer Cornfield"] = np.array(
        [[(347, 715), (326, 708), (325, 713), (284, 701), (261, 680)]])
    aerial_coordinates["University Checkpoint-Munchies"] = np.array([[(54, 633), (127, 670), (145, 694), (182, 794),
                                                                      (200, 828), (221, 855), (264, 887), (301, 908),
                                                                      (362, 920), (421, 942), (426, 954), (386, 971)]])
    aerial_coordinates["Munchies-University Checkpoint"] = np.array([[(386, 971), (426, 954), (421, 942), (362, 920),
                                                                      (301, 908), (264, 887), (221, 855), (200, 828),
                                                                      (182, 794), (145, 694), (127, 670), (54, 633)]])
    aerial_coordinates["University Checkpoint-Founders Plaza"] = np.array(
        [[(54, 633), (127, 670), (145, 694), (180, 774), (257, 813)]])
    aerial_coordinates["Founders Plaza-University Checkpoint"] = np.array(
        [[(257, 813), (180, 774), (145, 694), (127, 670), (54, 633)]])
    aerial_coordinates["Thacher Arboretum-Green Gate"] = np.array([[(154, 647), (175, 633), (222, 606)]])
    aerial_coordinates["Green Gate-Thacher Arboretum"] = np.array([[(222, 606), (175, 633), (154, 647)]])
    aerial_coordinates["University Checkpoint-Thacher Arboretum"] = np.array(
        [[(54, 633), (115, 661), (130, 660), (175, 633)]])
    aerial_coordinates["Thacher Arboretum-University Checkpoint"] = np.array(
        [[(175, 633), (130, 660), (115, 661), (54, 633)]])
    aerial_coordinates["Thacher Arboretum-Munchies"] = np.array([[(175, 633), (130, 660), (145, 694), (182, 794),
                                                                      (200, 828), (221, 855), (264, 887), (301, 908),
                                                                      (362, 920), (421, 942), (426, 954), (386, 971)]])
    aerial_coordinates["Munchies-Thacher Arboretum"] = np.array([[(386, 971), (426, 954), (421, 942), (362, 920),
                                                                      (301, 908), (264, 887), (221, 855), (200, 828),
                                                                      (182, 794), (145, 694),(130,660),(175,633)]])
    aerial_coordinates["The Hive-Porters' Lodge"] = np.array([[(456,724),(429,722),(429,736),(454,765),(487,783),(484,814)]])
    aerial_coordinates["Porters' Lodge-The Hive"] = np.array([[(484, 814),(487, 783), (454, 765),(429, 736), (429, 722),(456, 724)]])
    aerial_coordinates["Porters' Lodge-Munchies"] = np.array([[(482,836),(482,853),(493,874), (496,953),(484,960),(426,956),(400,963)]])
    aerial_coordinates["Munchies-Porters' Lodge"] = np.array([[(400, 963), (426, 956), (484, 960), (496, 953), (493, 874),(482, 853), (482, 836)]])
    aerial_coordinates["Mathaai Hall-Hall 2C"] = np.array([[(510,833),(563,831),(605,823),(604,817)]])
    aerial_coordinates["Hall 2C-Mathaai Hall"] = np.array([[(604, 817),(605, 823), (563, 831),(510, 833)]])
    aerial_coordinates["Porters' Lodge-Mathaai Hall"] = np.array([[(491,829),(506,830),(533,830)]])
    aerial_coordinates["Mathaai Hall-Porters' Lodge"] = np.array([[(533, 830),(506, 830),(491, 829)]])
    aerial_coordinates["Porters' Lodge-Tawiah Hall"] =np.array([[(496,829),(506,831),(534,866)]])
    aerial_coordinates["Tawiah Hall-Porters' Lodge"] = np.array([[(534,866),(506,831),(496,829)]])
    aerial_coordinates["The Grill-Porters' Lodge"] = np.array([[(406,743),(419,758),(433,760),(454,766),(485,782),(486,815)]])
    aerial_coordinates["Porters' Lodge-The Grill"] = np.array([[(486, 815), (485, 782),(454, 766),(433, 760), (419, 758),(406, 743)]])
    aerial_coordinates["Porters' Lodge-Amu Hall"] = np.array([[(469,827),(439,828)]])
    aerial_coordinates["Porters' Lodge-Sisulu Hall"] = np.array([[(482,839),(482,853),(465,877)]])
    aerial_coordinates["Sisulu Hall-Porters' Lodge"] = np.array([[(465, 877),(482, 853),(482, 839)]])
    aerial_coordinates["Amu Hall-Bliss Lounge"] = np.array([[(439,828),(404,829),(389,838),(389,831)]])
    aerial_coordinates["Bliss Lounge-Amu Hall"] = np.array([[(389, 831), (389, 838),(404, 829),(439, 828)]])
    aerial_coordinates["Bliss Lounge-Sutherland Hall"] = np.array([[(387,838),(363,838)]])
    aerial_coordinates["Sutherland Hall-Bliss Lounge"] = np.array([[(363, 838),(387, 838)]])
    aerial_coordinates["Bliss Lounge-Oteng Korankye II Hall"] = np.array([[(381,833),(381,843),(381,878),(379,878)]])
    aerial_coordinates["Oteng Korankye II Hall-Bliss Lounge"] = np.array([[ (379, 878),(381, 878), (381, 843), (381, 833)]])
    aerial_coordinates["Databank Foundation Hall-Sutherland Hall"] = np.array([[(365,755),(351,776),(341,777),(317,794),(319,823)]])
    aerial_coordinates["Sutherland Hall-Databank Foundation Hall"] = np.array([[(319, 823), (317, 794),  (341, 777), (351, 776),(365, 755)]])
    aerial_coordinates["Ashesi Bookshop-Nutor Hall"] = np.array([[(352,712),(361,690),(375,696)]])
    aerial_coordinates["Nutor Hall-Ashesi Bookshop"] = np.array([[ (375, 696),(361, 690),(352, 712)]])
    aerial_coordinates["Databank Foundation Hall-The Grill"] = np.array([[(362,757),(372,737)]])
    aerial_coordinates["The Grill-Databank Foundation Hall"] = np.array([[(372, 737),(362, 757)]])
    aerial_coordinates["Nutor Hall-The Grill"] = np.array([[(384,704),(374,735)]])
    aerial_coordinates["The Grill-Nutor Hall"] = np.array([[(374,735),(384,704)]])
    aerial_coordinates["The Hive-The Grill"] = np.array([[(472,722),(430,722),(430,737),(439,758),(439,758)]])
    aerial_coordinates["Apt Hall-Ashesi Bookshop"] = np.array([[(328,703),(348,713)]])
    aerial_coordinates["Ashesi Bookshop-Apt Hall"] = np.array([[(348, 713),(328, 703)]])

    return aerial_coordinates


def initalize_map():
    AshesiMap = Graph()

    AshesiMap.add_edge("Sports Centre", "Service Centre", 3)
    AshesiMap.add_edge("Service Centre", "Engineering Workshop", 2)
    AshesiMap.add_edge("Engineering Workshop", "Natembea Health Centre", 3)
    AshesiMap.add_edge("Natembea Health Centre", "Fab Lab", 1)
    AshesiMap.add_edge("Fab Lab", "Green Gate", 10)
    AshesiMap.add_edge("Green Gate", "Warren Library", 2)
    AshesiMap.add_edge("Green Gate", "King Engineering Building", 5)
    AshesiMap.add_edge("King Engineering Building", "Nutor Hall", 2)
    AshesiMap.add_edge("Radichel Hall", "Warren Library", 5)
    AshesiMap.add_edge("Warren Library", "Apt Hall", 3)
    AshesiMap.add_edge("Radichel Hall", "Jackson Hall", 2)
    AshesiMap.add_edge("Jackson Hall", "Archer Cornfield", 2)
    AshesiMap.add_edge("Jackson Hall", "Founders Plaza", 2)
    AshesiMap.add_edge("Radichel Hall", "Founders Plaza", 2)
    AshesiMap.add_edge("Apt Hall", "Archer Cornfield", 1)
    AshesiMap.add_edge("Archer Cornfield", "Databank Foundation Hall", 1)
    # AshesiMap.add_edge("Collins Courtyard", "Ashesi Bookshop", 1)
    AshesiMap.add_edge("University Checkpoint", "Munchies", 25)
    AshesiMap.add_edge("University Checkpoint", "Founders Plaza", 15)
    AshesiMap.add_edge("University Checkpoint", "Thacher Arboretum", 13)
    AshesiMap.add_edge("Green Gate", "Thacher Arboretum", 2)
    AshesiMap.add_edge("Munchies", "Thacher Arboretum", 12)
    AshesiMap.add_edge("Nutor Hall", "The Hive", 2)



    AshesiMap.add_edge("The Hive","Porters' Lodge",5)
    AshesiMap.add_edge("Porters' Lodge", "Munchies", 1)
    AshesiMap.add_edge("Porters' Lodge", "Mathaai Hall", 1)
    AshesiMap.add_edge("Porters' Lodge", "Tawiah Hall", 5)
    AshesiMap.add_edge("Mathaai Hall", "Hall 2C", 2)
    AshesiMap.add_edge("Tawiah Hall", "Hall 2D", 2)
    AshesiMap.add_edge("The Grill", "Porters' Lodge", 6)
    AshesiMap.add_edge("Porters' Lodge", "Amu Hall", 1)
    AshesiMap.add_edge("Porters' Lodge", "Sisulu Hall", 3)
    AshesiMap.add_edge("Amu Hall", 'Bliss Lounge', 1)
    AshesiMap.add_edge("Bliss Lounge", 'Sutherland Hall', 1)
    AshesiMap.add_edge("Bliss Lounge", 'Oteng Korankye II Hall', 3)
    AshesiMap.add_edge("Databank Foundation Hall", 'Sutherland Hall', 13)
    AshesiMap.add_edge("Ashesi Bookshop", 'Nutor Hall', 2)
    AshesiMap.add_edge("The Hive","The Grill", 5)
    AshesiMap.add_edge("Nutor Hall", 'The Grill', 3)
    AshesiMap.add_edge("Databank Foundation Hall", 'The Grill', 2)
    AshesiMap.add_edge("Apt Hall", "Ashesi Bookshop", 2)
    AshesiMap.add_edge("Ashesi Bookshop","Apt Hall", 2)





    AshesiMap.add_edge("Service Centre", "Sports Centre", 3)
    AshesiMap.add_edge("Engineering Workshop", "Service Centre", 2)
    AshesiMap.add_edge("Natembea Health Centre", "Engineering Workshop", 3)
    AshesiMap.add_edge("Fab Lab", "Natembea Health Centre", 1)
    AshesiMap.add_edge("Green Gate", "Fab Lab", 10)
    AshesiMap.add_edge("Warren Library", "Green Gate", 2)
    AshesiMap.add_edge("King Engineering Building", "Green Gate", 5)
    AshesiMap.add_edge("Nutor Hall", "King Engineering Building", 2)
    AshesiMap.add_edge("Warren Library", "Radichel Hall", 5)
    AshesiMap.add_edge("Apt Hall", "Warren Library", 3)
    AshesiMap.add_edge("Jackson Hall", "Radichel Hall", 2)
    AshesiMap.add_edge("Archer Cornfield", "Jackson Hall", 2)
    AshesiMap.add_edge("Founders Plaza", "Jackson Hall", 2)
    AshesiMap.add_edge("Founders Plaza", "Radichel Hall", 2)
    AshesiMap.add_edge("Archer Cornfield", "Apt Hall", 1)
    AshesiMap.add_edge("Databank Foundation Hall", "Archer Cornfield", 1)
    AshesiMap.add_edge("Munchies", "University Checkpoint", 25)
    AshesiMap.add_edge("Founders Plaza", "University Checkpoint", 15)
    AshesiMap.add_edge("Thacher Arboretum", "Green Gate", 2)
    AshesiMap.add_edge("Thacher Arboretum", "University Checkpoint", 13)
    AshesiMap.add_edge("Thacher Arboretum", "Munchies", 12)
    AshesiMap.add_edge("The Hive", "Nutor Hall", 2)



    AshesiMap.add_edge("Porters' Lodge","The Hive", 5)
    AshesiMap.add_edge('Munchies', "Porters' Lodge", 11)
    AshesiMap.add_edge('Mathaai Hall',"Porters' Lodge",  1)
    AshesiMap.add_edge('Tawiah Hall',"Porters' Lodge",  5)
    AshesiMap.add_edge("Hall 2C", "Mathaai Hall", 2)
    AshesiMap.add_edge('Hall 2D',"Tawiah Hall", 2)
    AshesiMap.add_edge("Porters' Lodge","The Grill", 6)
    AshesiMap.add_edge('Amu Hall',"Porters' Lodge", 1)
    AshesiMap.add_edge('Sisulu Hall',"Porters' Lodge", 3)
    AshesiMap.add_edge('Bliss Lounge',"Amu Hall", 1)
    AshesiMap.add_edge('SutherLand Hall',"Bliss Lounge", 1)
    AshesiMap.add_edge('Oteng Korankye II Hall', "Bliss Lounge", 3)
    AshesiMap.add_edge('Sutherland Hall',"Databank Foundation Hall",  13)
    AshesiMap.add_edge('Nutor Hall',"Ashesi Bookshop", 2)
    AshesiMap.add_edge("The Grill","The Hive",5)
    AshesiMap.add_edge('The Grill',"Nutor Hall", 3)
    AshesiMap.add_edge('The Grill',"Databank Foundation Hall", 2)

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
    heuristic_val = math.sqrt(x_squared + y_squared)
    return heuristic_val




def aStarSearch(problem):
    explored = set()
    predecessors = dict()
    transcost = dict()
    frontier = PriorityQueue()
    start = Node(problem.initial_state)
    print(start)
    transcost[start.state] = 0
    frontier.add(start)
    maxl = len(frontier)

    while frontier:
        node = frontier.pop()
        print("popped node: ", node)
        print("frontier: ", frontier)

        if node.state in explored:
            continue

        if (problem.goal_test(node.state)):
            print("Found a solution! ", node)
            print("Max frontier length: ", maxl)
            print("Nodes processed: ", len(explored))
            path = solution_path(predecessors, problem.initial_state, problem.goal_state)
            return path

        explored.add(node.state)
        print("explored: ", explored)
        successors = problem.actions(node.state)
        print("successors: ", successors)
        for i in range(len(successors)):
            child = successors[i]
            distance = successors[i].path_cost
            added_cost = transcost[node.state] + distance

            if child.state not in transcost or added_cost < transcost[child.state]:
                transcost[child.state] = added_cost
                priority = added_cost + heuristic(child.state,problem.goal_state,problem.pixel_dict)
                frontier.add(child,priority)
                if  len(frontier) > maxl:
                    maxl = len(frontier)
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


def display_path(solution):
    list = []
    for i in range(len(solution) - 1):
        list.append(myProb.aerial_coordinates[solution[i] + "-" + solution[i + 1]])

    array = list[0]
    for i in range(len(list) - 1):
        array = np.append(array, list[i + 1], axis=1)

    cv2.polylines(image,array,isClosed=False,color=(0, 0, 230),thickness=3)
    coordinates = array[-1][-1]
    radius = 15
    color = (255, 0, 0)
    thickness = -1
    cv2.circle(image,coordinates,radius,color,thickness)
    plt.imshow(image)
    plt.show()


def home_button_event():
    pass



def change_appearance_mode_event(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)


def login():
    start = combobox_1.get()
    destination = combobox_2.get()

    global myProb
    myProb = CampusNavigationProb(start, destination)
    myProb.display_prob()
    solution = aStarSearch(myProb)
    print(solution)
    display_path(solution)








if __name__ == "__main__":
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("green")

    root = customtkinter.CTk()
    root.title("Campus Navigation System")

    root.geometry("700x450")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    navigation_frame = customtkinter.CTkFrame(root, corner_radius=0)
    navigation_frame.grid(row=0, column=0, sticky="nsew")
    navigation_frame.grid_rowconfigure(4, weight=1)

    navigation_frame_label = customtkinter.CTkLabel(navigation_frame, text="Welcome!",
                                                         compound="left",
                                                         font=customtkinter.CTkFont(size=15, weight="bold"))
    navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

    home_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40,
                                               border_spacing=10, text="Home",
                                               fg_color="transparent", text_color=("gray10", "gray90"),
                                               hover_color=("gray70", "gray30"),
                                               anchor="w", command=home_button_event)
    home_button.grid(row=1, column=0, sticky="ew")

    appearance_mode_menu = customtkinter.CTkOptionMenu(navigation_frame,
                                                            values=["Light", "Dark", "System"],
                                                            command=change_appearance_mode_event)
    appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

    # create home frame
    home_frame = customtkinter.CTkFrame(root, corner_radius=0, fg_color="transparent")
    home_frame.grid_columnconfigure(0, weight=1)
    home_frame.grid(row=0, column=1, sticky="nsew")

    label = customtkinter.CTkLabel(home_frame, text="Campus Navigation System", font=("Roboto", 24))
    label.grid(row=1, column=0, padx=20, pady=20)
    landmarks = ["Radichel Hall", "Warren Library", "Apt Hall", "Jackson Hall", "Databank Foundation Hall",
                 "Ashesi Bookshop", "King Engineering Building", "Nutor Hall", "Fab Lab",
                 "Engineering Workshop",
                 "The Hive", "The Grill", "Bliss Lounge", "Natembea Health Centre", "Archer Cornfield",
                 "Founders Plaza", "Porters' Lodge", "Thacher Arboretum", "Sutherland Hall", "Amu Hall",
                 "Mathaai Hall",
                 "Hall 2C", "Oteng Korankye II Hall", "Sisulu Hall", "Tawiah Hall", "Hall 2D", "Service Centre",
                 "University Checkpoint", "Green Gate", "Munchies", "Sports Centre"]
    landmarks.sort()

    combobox_1 = customtkinter.CTkComboBox(home_frame, values=landmarks)
    combobox_1.grid(row=2, column=0, pady=10, padx=10)

    combobox_2 = customtkinter.CTkComboBox(home_frame, values=landmarks)
    combobox_2.grid(row=3, column=0, pady=10, padx=10)

    button_1 = customtkinter.CTkButton(home_frame, command=login)
    button_1.grid(row=4, column=0, pady=10, padx=10)

    root.mainloop()





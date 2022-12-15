import customtkinter
import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
from Graph import *
from PriorityQueue import *
from Problem import *
from Search import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("Campus Navigation System")

def login():
    start = combobox_1.get()
    destination = combobox_2.get()
    myProb = CampusNavigationProb(start, destination)
    myProb.display_prob()
    solution = aStarSearch(myProb)
    print(solution)
    display_path(solution)


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand =True)

label = customtkinter.CTkLabel(master=frame, text = "Navigation System", font=("Roboto",24))
label.pack(pady=12,padx=10)

landmarks = ["Radichel Hall", "Warren Library", "Apt Hall","Jackson Hall","Databank Foundation Hall","Ashesi Bookshop","King Engineering Building","Nutor Hall","Fab Lab","Engineering Workshop","The Hive","The Grill","Bliss Lounge","Natembea Health Centre","Archer Cornfield","Founders Plaza","Porters' Lodge","Thacher Arboretum","Sutherland Hall","Amu Hall","Mathaai Hall","Hall 2C","Oteng Korankye II Hall","Sisulu Hall","Tawiah Hall","Hall 2D","Service Centre","University Checkpoint","Green Gate","Munchies"]
landmarks.sort()

combobox_1 = customtkinter.CTkComboBox(frame, values=landmarks)
combobox_1.pack(pady=10, padx=10)

combobox_2 = customtkinter.CTkComboBox(frame,values=landmarks)
combobox_2.pack(pady=10,padx=10)

button_1 = customtkinter.CTkButton(master=frame, command=login)
button_1.pack(pady=10, padx=10)

root.mainloop()



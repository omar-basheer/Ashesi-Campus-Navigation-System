

import customtkinter
from Search import *


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("image_example.py")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Image Example",
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")


        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid(row=0, column=1, sticky="nsew")

        self.label = customtkinter.CTkLabel(self.home_frame,text="Campus Navigation System",font=("Roboto",24))
        self.label.grid(row=1,column=0,padx=20,pady = 20)
        landmarks = ["Radichel Hall", "Warren Library", "Apt Hall", "Jackson Hall", "Databank Foundation Hall",
                     "Ashesi Bookshop", "King Engineering Building", "Nutor Hall", "Fab Lab", "Engineering Workshop",
                     "The Hive", "The Grill", "Bliss Lounge", "Natembea Health Centre", "Archer Cornfield",
                     "Founders Plaza", "Porters' Lodge", "Thacher Arboretum", "Sutherland Hall", "Amu Hall", "Mathaai Hall",
                     "Hall 2C", "Oteng Korankye II Hall", "Sisulu Hall", "Tawiah Hall", "Hall 2D", "Service Centre",
                     "University Checkpoint", "Green Gate", "Munchies","Sports Centre"]
        landmarks.sort()

        combobox_1 = customtkinter.CTkComboBox(self.home_frame, values=landmarks)
        combobox_1.grid(row = 2, column = 0, pady=10, padx=10)

        combobox_2 = customtkinter.CTkComboBox(self.home_frame, values=landmarks)
        combobox_2.grid(row=3, column = 0, pady=10, padx=10)

        button_1 = customtkinter.CTkButton(self.home_frame, command=login)
        button_1.grid(row=4, column = 0, pady=10, padx=10)



    def home_button_event(self):
        pass



    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)



def login(x,y):
    start = x.get()
    destination = y.get()

    global myProb
    myProb = CampusNavigationProb(start, destination)
    myProb.display_prob()
    solution = aStarSearch(myProb)
    print(solution)
    display_path(solution)


if __name__ == "__main__":
    app = App()
    app.mainloop()



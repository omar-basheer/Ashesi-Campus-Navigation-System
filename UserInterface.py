import customtkinter
from Search import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

def login():
    print("Test")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand =True)

label = customtkinter.CTkLabel(master=frame, text = "Navigation System", font=("Roboto",24))
label.pack(pady=12,padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Start")
entry1.pack(pady=12,padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Goal")
entry2.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame, text="Search",command=login)
button.pack(pady=12,padx=10)

root.mainloop()



myProb = CampusNavigationProb(entry1.get(), "The Hive")
myProb.display_prob()

solution = aStarSearch(myProb)
print(solution)
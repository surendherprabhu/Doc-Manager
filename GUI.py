import customtkinter as ctk
import os
import tkinter as tk
from DSA  import *
from App import *


class GUI:
    def __init__(self):
        self.root = ctk.CTk()
        self.app = App()
        self.create_window(self.root)

    def on_enter(self,event):
        self.sort_button.configure(border_width=2, font=("Arial", 14, "bold"))

    def on_leave(self,event):
        self.sort_button.configure(border_width=0, font=("Arial", 13))

    def on_click(self,event):
        self.sort_button.place_configure(rely=0.51) # Moves slightly down

    def on_release(self,event):
        self.sort_button.place_configure(rely=0.5) # Returns to center

    def create_window(self , window , width = 960, height = 540):


        self.window = window
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        self.scaling = self.window._get_window_scaling()

        x = int(((self.screen_width / 2) - (width / 2)) * self.scaling)
        y = int(((self.screen_height / 2) - (height / 2)) * self.scaling)
        
        self.window.geometry(f"{width}x{height}+{x}+{y}")

        self.sort_button = ctk.CTkButton(master=self.root, 
                    text="SORT", 
                    corner_radius=20,     
                    border_width=2, 
                    fg_color="transparent", 
                    hover_color="#12C0DF", 
                    border_color="#220349",
                    command=self.sort)
        self.sort_button.place(relx=0.5, rely=0.5, anchor="center")
        
        self.sort_button.bind("<Enter>", self.on_enter)
        self.sort_button.bind("<Leave>", self.on_leave)
        self.sort_button.bind("<ButtonPress-1>", self.on_click)
        self.sort_button.bind("<ButtonRelease-1>", self.on_release)

        self.create_button = ctk.CTkButton(master=self.root, 
                    text="SORT", 
                    corner_radius=20,     
                    border_width=2, 
                    fg_color="transparent", 
                    hover_color="#12C0DF", 
                    border_color="#220349",
                    command=self.sort)
        self.sort_button.place(relx=0.5, rely=0.5, anchor="center")
        
        self.sort_button.bind("<Enter>", self.on_enter)
        self.sort_button.bind("<Leave>", self.on_leave)
        self.sort_button.bind("<ButtonPress-1>", self.on_click)
        self.sort_button.bind("<ButtonRelease-1>", self.on_release)

        self.root.mainloop()

    def sort(self):
        self.app.sort()


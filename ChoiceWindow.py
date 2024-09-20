# choice_window.py
from Window import Window
import tkinter as tk

class ChoiceWindow(Window):
    def __init__(self, main_app, title, width, height):
        super().__init__(main_app, title, width, height)

        self.choice_label = tk.Label(self.window, text="", font=('Calibri', 24))
        self.choice_label.pack(expand=True)

        self.hide()  # Initially hide the window

    def update_choice(self, choice):
        choices = ["Rock", "Paper", "Scissors"]
        if choice in [0, 1, 2]:
            self.choice_label.config(text=f"{choices[choice]}")
        elif choice is None:
            self.choice_label.config(text="No choice detected")
        else:
            self.choice_label.config(text="")

    def position_window(self, x, y):
        self.window.geometry(f'{self.width}x{self.height}+{x}+{y}')

    def show(self):
        super().show()
        self.choice_label.config(text="")  # Clear the choice when showing the window

    def hide(self):
        super().hide()
        self.choice_label.config(text="")  # Clear the choice when hiding the window
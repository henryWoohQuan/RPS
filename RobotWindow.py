# robot_window.py
from Window import Window
import tkinter as tk

class RobotWindow(Window):
    def __init__(self, main_app):
        width = main_app.screen_width // 3
        height = int(width * 0.75)  # 4:3 aspect ratio
        super().__init__(main_app, "Robot", width, height)

        self.robot_label = tk.Label(self.window, text="Robot", font=('Calibri', 48))
        self.robot_label.pack(expand=True)

        self.position_right()
        self.hide()  # Initially hide the window

    def position_right(self):
        x = self.main_app.screen_width - self.width
        y = (self.main_app.screen_height - self.height) // 2
        self.window.geometry(f'{self.width}x{self.height}+{x}+{y}')
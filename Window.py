# window.py
import tkinter as tk

class Window:
    def __init__(self, main_app, title, width, height):
        self.main_app = main_app
        self.window = tk.Toplevel()
        self.window.title(title)
        self.width = width
        self.height = height
        self.position()

    def position(self):
        # Default to center, can be overridden
        x = (self.main_app.screen_width - self.width) // 2
        y = (self.main_app.screen_height - self.height) // 2
        self.window.geometry(f'{self.width}x{self.height}+{x}+{y}')

    def show(self):
        self.window.deiconify()

    def hide(self):
        self.window.withdraw()

    def update(self):
        # To be implemented by child classes
        pass
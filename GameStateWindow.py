# game_state_window.py
from Window import Window
import tkinter as tk

class GameStateWindow(Window):
    def __init__(self, main_app):
        width = main_app.screen_width // 4
        height = main_app.screen_height // 4
        super().__init__(main_app, "Game State", width, height)

        self.state_label = tk.Label(self.window, text="", font=('Calibri', 36))
        self.state_label.pack(expand=True)

        self.hide()  # Initially hide the window

    def update_text(self, text):
        self.state_label.config(text=text)